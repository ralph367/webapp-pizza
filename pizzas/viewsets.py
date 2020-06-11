from rest_framework import viewsets

from .serializers import PizzasSerializer
from .models import Pizzas


class PizzasViewSet(viewsets.ModelViewSet):
    queryset = Pizzas.objects.all().order_by('id')
    serializer_class = PizzasSerializer