import pytest
from product.factories import CategoryFactory
from product.serializers import CategorySerializer

@pytest.mark.django_db
def test_category_serializer_accepts_valid_data():
    data = {
        "title": "Eletrônicos",
        "slug": "eletronicos",
        "description": "Produtos eletrônicos",
        "active": True,

    }

    serializer = CategorySerializer(data=data)

    assert serializer.is_valid(), serializer.errors



@pytest.mark.django_db
def test_category_serializer_returns_category_data():
    category = CategoryFactory()

    serializer = CategorySerializer(category)

    assert serializer.data["title"] == category.title
    assert serializer.data["slug"] == category.slug
    assert serializer.data["description"] == category.description
    assert serializer.data["active"] == category.active


@pytest.mark.django_db
def test_category_serializer_requires_title():
    data = {
        "slug": "eletronicos",
        "description": "Produtos eletrônicos",
        "active": True,
    }

    serializer = CategorySerializer(data=data)

    assert not serializer.is_valid()
    assert "title" in serializer.errors


@pytest.mark.django_db
def test_category_serializer_requires_slug():
    data = {
        "title": "Eletrônicos",
        "description": "Produtos eletrônicos",
        "active": True,

    }

    serializer = CategorySerializer(data=data)

    assert not serializer.is_valid()
    assert "slug" in serializer.errors
