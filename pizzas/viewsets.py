from rest_framework import viewsets
from .serializers import PizzasSerializer
from .models import Pizzas


class PizzasViewSet(viewsets.ModelViewSet):
    """Viewset of Pizza model with existing base classes that provide a default set of behavior
    """
    queryset = Pizzas.objects.all().order_by('id')
    serializer_class = PizzasSerializer
