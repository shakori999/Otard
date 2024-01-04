from ecommerce.inventory.models import Category
import pytest

@pytest.mark.django_db
def test_name_max_length(single_category):
    assert len(single_category.name) <= 100  # Assuming the maximum length is 100 characters

@pytest.mark.django_db
def test_slug_uniqueness(single_category):
    # Creating a new category with the same slug should raise an IntegrityError
    with pytest.raises(Exception):  # Adjust the expected exception based on your specific error handling
        Category.objects.create(name='Another Category', slug='test-category')

@pytest.mark.django_db
def test_is_active_default_value(single_category):
    assert single_category.is_active is True  # Assuming the default value is set to True

@pytest.mark.django_db
def test_cannot_be_own_parent(create_categories):
    root_category = create_categories['root_category']
    with pytest.raises(Exception):  # Adjust the expected exception based on your specific error handling
        root_category.parent = root_category
        root_category.save()

@pytest.mark.django_db
def test_null_or_blank_parent(create_categories):
    root_category = create_categories['root_category']
    child_category = create_categories['category_1']

    # Test setting parent as null
    child_category.parent = None
    child_category.save()
    assert child_category.parent is None

    # Test setting parent as blank
    child_category.parent = root_category
    child_category.save()
    assert child_category.parent == root_category


@pytest.mark.django_db
def test_check_categories_ordering(create_categories):
    categories = create_categories

    # Check that the ordering within the tree is maintained properly
    assert list(categories['root_category'].get_children()) == [categories['category_1'], categories['category_2']]
    assert list(categories['category_1'].get_children()) == [categories['subcategory_1']]

@pytest.mark.django_db
def test_tree_integrity_after_crud(create_categories):
    root_category = create_categories['root_category']
    category_1 = create_categories['category_1']
    category_2 = create_categories['category_2']
    subcategory_1 = create_categories['subcategory_1']

    # Creating a new category under root
    new_category = Category.objects.create(name='New Category', slug='new-category', parent=root_category)
    assert list(root_category.get_children()) == [category_1,category_2,new_category]

    # Updating the subcategory_1 to change its parent to category_2
    subcategory_1.parent = category_2
    subcategory_1.save()
    assert list(category_2.get_children()) == [subcategory_1]
    print(category_2.get_children())

    # Deleting category_2
    subcategory_1.delete()
    category_2.delete()
    print(root_category.get_children())
    assert list(root_category.get_children()) == [category_1, new_category]
