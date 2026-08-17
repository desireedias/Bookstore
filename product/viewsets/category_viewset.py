from rest_framework.viewsets import ModelViewSet

from product.serializers import CategorySerializer
from product.models import Category


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all().order_by("id")
