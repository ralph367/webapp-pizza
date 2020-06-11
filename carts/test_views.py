import json
from rest_framework import status
from rest_framework.test import APIClient
from django.test import TestCase, Client
from django.urls import reverse
from .models import Carts
from pizzas.models import Pizzas
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


class AddToCart(TestCase):
    """ Testing to GET all carts API """

    def setUp(self):
        Pizzas.objects.create(name="peperoni", category="ham", price=1)
        Pizzas.objects.create(name="peperoniii", category="ham", price=11)
        self.valid_payload = {
            'id': '1',
            'amount': '1'
        }
        self.invalid_payload_negative = {
            'id': '2',
            'amount': '-1',
        }
        self.invalid_payload_wrongpizza = {
            'id': '6',
            'amount': '1',
        }
        self.invalid_payload_notint = {
            'id': 'asd',
            'amount': 'asdd',
        }

    def test_add_session_valid_payload(self):
        # post API response
        response = client.post(
            reverse('addtocart'),
            data=self.valid_payload
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_add_session_invalid_negative(self):
        # post API response
        response = client.post(
            reverse('addtocart'),
            data=self.invalid_payload_negative
        )
        self.assertEqual(response.status_code, status.HTTP_406_NOT_ACCEPTABLE)

    def test_add_session_invalid_wrongpizza(self):
        # post API response
        response = client.post(
            reverse('addtocart'),
            data=self.invalid_payload_wrongpizza
        )
        self.assertEqual(response.status_code, status.HTTP_501_NOT_IMPLEMENTED)

    def test_add_session_invalid_notint(self):
        # post API response
        response = client.post(
            reverse('addtocart'),
            data=self.invalid_payload_notint
        )
        self.assertEqual(response.status_code,
                         status.HTTP_417_EXPECTATION_FAILED)


class UpdateCart(TestCase):
    """ Testing to GET all carts API """

    def setUp(self):
        Pizzas.objects.create(name="peperoni", category="ham", price=1)
        Pizzas.objects.create(name="peperoniii", category="ham", price=11)
        self.valid_payload = {
            'id': '1',
            'amount': '1'
        }
        self.invalid_payload_negative = {
            'id': '2',
            'amount': '-1',
        }
        self.invalid_payload_wrongpizza = {
            'id': '6',
            'amount': '1',
        }
        self.invalid_payload_notint = {
            'id': 'asd',
            'amount': 'asdd',
        }

    def test_update_unavailablesession(self):
        # post API response
        response = client.post(
            reverse('updatecart'),
            data=self.valid_payload
        )
        self.assertEqual(response.status_code,
                         status.HTTP_412_PRECONDITION_FAILED)

    def test_update_session_valid_payload(self):
        session = self.client.session
        session['cart'] = [
            {'id': 1, 'amount': 1, 'description': 'Salami', 'name': 'Peperoni', 'price': '10.2'}]
        session.save()
        # post API response
        response = self.client.post(
            reverse('updatecart'),
            data=self.valid_payload
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_session_invalid_negative(self):
        session = self.client.session
        session['cart'] = [
            {'id': 1, 'amount': 1, 'description': 'Salami', 'name': 'Peperoni', 'price': '10.2'}]
        session.save()
        # post API response
        response = self.client.post(
            reverse('updatecart'),
            data=self.invalid_payload_negative
        )
        self.assertEqual(response.status_code, status.HTTP_406_NOT_ACCEPTABLE)

    def test_update_session_invalid_wrongpizza(self):
        session = self.client.session
        session['cart'] = [
            {'id': 1, 'amount': 1, 'description': 'Salami', 'name': 'Peperoni', 'price': '10.2'}]
        session.save()
        # post API response
        response = self.client.post(
            reverse('updatecart'),
            data=self.invalid_payload_wrongpizza
        )
        self.assertEqual(response.status_code, status.HTTP_501_NOT_IMPLEMENTED)

    def test_update_session_invalid_notint(self):
        session = self.client.session
        session['cart'] = [
            {'id': 1, 'amount': 1, 'description': 'Salami', 'name': 'Peperoni', 'price': '10.2'}]
        session.save()
        # post API response
        response = self.client.post(
            reverse('updatecart'),
            data=self.invalid_payload_notint
        )
        self.assertEqual(response.status_code,
                         status.HTTP_417_EXPECTATION_FAILED)


class CartCost(TestCase):
    """ Testing to GET all carts API """

    def setUp(self):
        Pizzas.objects.create(name="peperoni", price=12.5)
        Pizzas.objects.create(name="peperoniii", price=9)

    def test_cart_cost_valid(self):
        session = self.client.session
        session['cart'] = [
            {'id': 1, 'amount': 2}]
        session.save()
        # post API response
        response = self.client.get(reverse('totalcost'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.content.decode('utf-8'), str(2 * 12.5))

    def test_cart_cost_unavailable_pizza(self):
        session = self.client.session
        session['cart'] = [
            {'id': 4, 'amount': 2}]
        session.save()
        # post API response
        response = self.client.get(reverse('totalcost'))
        self.assertEqual(response.status_code, status.HTTP_501_NOT_IMPLEMENTED)
        self.assertEqual(response.content.decode('utf-8'), "Unavailable Pizza")

    def test_empty_cart_cost(self):
        # post API response
        response = self.client.get(reverse('totalcost'))
        self.assertEqual(response.status_code, status.HTTP_412_PRECONDITION_FAILED)
        self.assertEqual(response.content.decode('utf-8'), "Cart is empty")