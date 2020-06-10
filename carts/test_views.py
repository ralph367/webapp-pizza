import json
from rest_framework import status
from rest_framework.test import APIClient
from django.test import TestCase, Client
from django.urls import reverse
from .models import Carts
from .serializers import CartsSerializer


# initialize the APIClient app
client = Client()
apiclient = APIClient()


class GetAllCartsTest(TestCase):
    """ Testing to GET all carts API """

    def setUp(self):
        Carts.objects.create(price="1")
        Carts.objects.create(price="2")
        Carts.objects.create(price="3")
        Carts.objects.create(price="4")

    def test_get_all_carts(self):
        # get API response
        response = apiclient.get('/carts/')
        # get data from db
        carts = Carts.objects.all()
        serializer = CartsSerializer(carts, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

