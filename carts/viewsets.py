from rest_framework import viewsets

from .serializers import CartsSerializer
from .models import Carts


class CartsViewSet(viewsets.ModelViewSet):
    queryset = Carts.objects.all().order_by('cart_id')
    serializer_class = CartsSerializer