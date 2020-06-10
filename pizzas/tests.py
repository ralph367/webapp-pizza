from django.test import TestCase
from .serializers import PizzasSerializer
from .models import Pizzas


class PizzaTest(TestCase):
    """ Test module for Pizza model """

    def setUp(self):
        Pizzas.objects.create(name="peperoni", category="ham")
        Pizzas.objects.create(name="marg", category="vegi")

    def test_pizza_category(self):
        pizzapep = Pizzas.objects.get(name='peperoni')
        pizzamarg = Pizzas.objects.get(name='marg')
        self.assertEqual(pizzapep.get_pizza(), "peperoni in category ham")
        self.assertEqual(pizzamarg.get_pizza(), "marg in category vegi")


