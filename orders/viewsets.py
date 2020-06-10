from rest_framework import viewsets

from .serializers import OrdersSerializer
from .models import Orders


class OrdersViewSet(viewsets.ModelViewSet):
    queryset = Orders.objects.all().order_by('order_id')
    serializer_class = OrdersSerializer