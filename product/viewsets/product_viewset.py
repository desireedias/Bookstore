from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated


from product.serializers import ProductSerializer
from product.models import Product


class ProductViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]

    serializer_class = ProductSerializer
    queryset = Product.objects.all()
