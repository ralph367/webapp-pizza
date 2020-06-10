from django.test import TestCase
from .serializers import PizzasSerializer
from .models import Pizzas


class PizzaTest(TestCase):
    """ Test module for Pizza model """

    def setUp(self):
        Pizzas.objects.create(pizza_name="peperoni", pizza_category="ham")
        Pizzas.objects.create(pizza_name="marg", pizza_category="vegi")

    def test_pizza_category(self):
        pizzapep = Pizzas.objects.get(pizza_name='peperoni')
        pizzamarg = Pizzas.objects.get(pizza_name='marg')
        self.assertEqual(pizzapep.get_pizza(), "peperoni in category ham")
        self.assertEqual(pizzamarg.get_pizza(), "marg in category vegi")


