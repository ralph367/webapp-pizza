import json
from rest_framework import status
from rest_framework.test import APIClient
from django.test import TestCase, Client
from django.urls import reverse
from .models import Orders
from pizzas.models import Pizzas
from .serializers import OrdersSerializer


# initialize the APIClient app
client = Client()
apiclient = APIClient()


class GetAllOrdersTest(TestCase):
    """ Testing to GET all orders API """

    def setUp(self):
        Orders.objects.create(price="1")
        Orders.objects.create(price="2")
        Orders.objects.create(price="3")
        Orders.objects.create(price="4")

    def test_get_all_orders(self):
        # get API response
        response = apiclient.get('/orders/')
        # get data from db
        orders = Orders.objects.all()
        serializer = OrdersSerializer(orders, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class PostOrderTest(TestCase):
    """ Testing to GET all orders API """

    def setUp(self):
        Pizzas.objects.create(name="Peperoni", category="Salami", price=10.2)
        Pizzas.objects.create(name="peperonii", category="hamm", price=1)
        Pizzas.objects.create(name="peperoniii", category="hammm", price=1)
        Pizzas.objects.create(name="pepii", category="hamm", price=1)
        self.valid_payload = {
            'price': 10.2,
            'currency': 'euro',
            'location': 'test',
            'phone': 'test',
            'addition_info': 'est',
            'name': 'asd'
        }

    def test_post_order(self):
        session = apiclient.session
        session['cart'] = [
            {'id': 1, 'amount': 1, 'description': 'Salami', 'name': 'Peperoni', 'price': '10.2'}]
        session.save()
        # get API response
        response = apiclient.post('/orders/',
            data=self.valid_payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)