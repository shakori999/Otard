import pytest
from ecommerce.inventory.models import Category

@pytest.mark.django_db
def test_category_creation(single_category):
    # Retrieve the created category using the fixture
    category = single_category

    # Verify that the category instance is created properly
    assert category.name == "Test Category"
    assert category.slug == "test-category"
    assert category.is_active == True
    
@pytest.mark.django_db
def test_category_str_method(single_category):
    # Retrieve the created category using the fixture
    category = single_category

    # Test the __str__ method of the Category model
    assert str(category) == "Test Category"

@pytest.mark.django_db
def test_get_id_category_correct(single_category):
    new_category = single_category
    get_category = Category.objects.all().first()
    assert new_category.id == get_category.id


def test_create_category_with_child(category_with_child):
    new_sub_category = category_with_child
    get_category = Category.objects.all().first()
    assert get_category.children.first().id == new_sub_category.id

@pytest.mark.django_db
def test_verify_tree_structure(create_categories):
    categories = create_categories

    # Verify the parent-child relationships
    assert categories['category_1'].parent == categories['root_category']
    assert categories['category_2'].parent == categories['root_category']
    assert categories['subcategory_1'].parent == categories['category_1']

@pytest.mark.django_db
def test_move_categories(create_categories):
    categories = create_categories

    # Ensure moving categories around in the hierarchy works as expected
    categories['subcategory_1'].parent = categories['category_2']
    assert categories['subcategory_1'].parent == categories['category_2']

