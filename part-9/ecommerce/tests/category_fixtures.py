import pytest
from ecommerce.inventory.models import Category

@pytest.fixture
def single_category(db):
    return Category.objects.create(name="Test Category", slug="test-category", is_active=True)

@pytest.fixture
def create_categories(db):
    # Create multiple categories with parent-child relationships
    root_category = Category.objects.create(name="Root Category", slug="root-category", is_active=True)
    category_1 = Category.objects.create(name="Category 1", slug="category-1", is_active=True, parent=root_category)
    category_2 = Category.objects.create(name="Category 2", slug="category-2", is_active=True, parent=root_category)
    subcategory_1 = Category.objects.create(name="Subcategory 1", slug="subcategory-1", is_active=True, parent=category_1)

    return {
        'root_category': root_category,
        'category_1': category_1,
        'category_2': category_2,
        'subcategory_1': subcategory_1,
    }

@pytest.fixture
def category_with_child(db):
    parent = Category.objects.create(name="parent", slug="parent")
    parent.children.create(name="child", slug="child")
    child = parent.children.first()
    return child


@pytest.fixture
def category_with_multiple_children(db):
    record = Category.objects.build_tree_nodes(
        {
            "id": 1,
            "name": "parent",
            "slug": "parent",
            "children": [
                {
                    "id": 2,
                    "parent_id": 1,
                    "name": "child",
                    "slug": "child",
                    "children": [
                        {
                            "id": 3,
                            "parent_id": 2,
                            "name": "grandchild",
                            "slug": "grandchild",
                        }
                    ],
                }
            ],
        }
    )
    category = Category.objects.bulk_create(record)
    return category
