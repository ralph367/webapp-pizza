import json
from rest_framework import status
from rest_framework.test import APIClient
from django.test import TestCase, Client
from django.urls import reverse
from .models import Orders
from .serializers import OrdersSerializer


# initialize the APIClient app
client = Client()
apiclient = APIClient()


class GetAllOrdersTest(TestCase):
    """ Testing to GET all orders API """

    def setUp(self):
        Orders.objects.create(order_price="1")
        Orders.objects.create(order_price="2")
        Orders.objects.create(order_price="3")
        Orders.objects.create(order_price="4")

    def test_get_all_orders(self):
        # get API response
        response = apiclient.get('/orders/')
        # get data from db
        orders = Orders.objects.all()
        serializer = OrdersSerializer(orders, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

