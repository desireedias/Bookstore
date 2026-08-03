import pytest

from product.factories import ProductFactory
from product.serializers import ProductSerializer


@pytest.mark.django_db
def test_product_serializer_accepts_valid_data():
    data = {
        "title": "Teclado",
        "description": "Teclado mecânico",
        "price": 150,
        "active": True,
        "category": [
            {
                "title": "Eletrônicos",
                "slug": "eletronicos",
                "description": "Produtos eletrônicos",
                "active": True,
            }
        ],
    }

    serializer = ProductSerializer(data=data)
    assert serializer.is_valid(), serializer.errors


@pytest.mark.django_db
def test_product_serializer_returns_valid_data():
    product = ProductFactory()

    serializer = ProductSerializer(product)

    assert serializer.data["title"] == product.title
    assert serializer.data["price"] == product.price
    assert serializer.data["active"] == product.active


@pytest.mark.django_db
def test_product_serializer_requires_title():
    data = {
        "description": "Produto sem título",
        "price": 150,
        "active": True,
        "category": [],
    }

    serializer = ProductSerializer(data=data)

    assert not serializer.is_valid()
    assert "title" in serializer.errors


@pytest.mark.django_db
def test_product_serializer_returns_category():
    product = ProductFactory()

    serializer = ProductSerializer(product)

    assert len(serializer.data["category"]) == 1
