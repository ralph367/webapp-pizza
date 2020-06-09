import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from .models import Orders
from .serializers import OrdersSerializer


# initialize the APIClient app
client = Client()


class GetAllPizzasTest(TestCase):
    """ Testing to GET all pizzas API """

    def setUp(self):
        Orders.objects.create(order_price="1")
        Orders.objects.create(order_price="2")
        Orders.objects.create(order_price="3")
        Orders.objects.create(order_price="4")

    def test_get_all_pizzas(self):
        # get API response
        response = client.get(reverse('home'))
        # get data from db
        pizzas = Orders.objects.all()
        serializer = OrdersSerializer(pizzas, many=True)
        self.assertEqual(response.orders, pizzas)

