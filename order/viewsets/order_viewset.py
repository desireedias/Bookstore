from rest_framework.viewsets import ModelViewSet

from order.serializers import OrderSerializer
from order.models import Order


class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all().order_by("id")
