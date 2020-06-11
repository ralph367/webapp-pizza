import json
from rest_framework import status
from rest_framework.test import APIClient
from django.test import TestCase, Client
from django.urls import reverse
from .models import Pizzas
from .serializers import PizzasSerializer


# initialize the APIClient app
client = Client()
apiclient = APIClient()


class GetAllPizzasTest(TestCase):
    """ Testing to GET all pizzas API """

    def setUp(self):
        Pizzas.objects.create(name="peperoni", category="ham", price=1)
        Pizzas.objects.create(name="peperonii", category="hamm", price=1)
        Pizzas.objects.create(name="peperoniii", category="hammm", price=1)
        Pizzas.objects.create(name="pepii", category="hamm", price=1)

    def test_get_all_pizzas(self):
        # get API response
        response = apiclient.get('/pizzas/')
        # get data from db
        pizzas = Pizzas.objects.all()
        serializer = PizzasSerializer(pizzas, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
