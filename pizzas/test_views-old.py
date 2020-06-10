import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from .models import Pizzas
from .serializers import PizzasSerializer


# initialize the APIClient app
client = Client()


class GetAllPizzasTest(TestCase):
    """ Testing to GET all pizzas API """

    def setUp(self):
        Pizzas.objects.create(pizza_name="peperoni", pizza_category="ham")
        Pizzas.objects.create(pizza_name="peperonii", pizza_category="hamm")
        Pizzas.objects.create(pizza_name="peperoniii", pizza_category="hammm")
        Pizzas.objects.create(pizza_name="peperoniiii",
                              pizza_category="hammmm")

    def test_get_all_pizzas(self):
        # get API response
        response = client.get(reverse('get_post_pizzas'))
        # get data from db
        pizzas = Pizzas.objects.all()
        serializer = PizzasSerializer(pizzas, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSinglePizzaTest(TestCase):
    """ Testing to GET single pizza API """

    def setUp(self):
        """ Dummy entries into the pizzas table """
        self.pizza1 = Pizzas.objects.create(
            pizza_name="peperoni", pizza_category="ham")
        self.pizza2 = Pizzas.objects.create(
            pizza_name="peperonii", pizza_category="hamm")
        self.pizza3 = Pizzas.objects.create(
            pizza_name="peperoniii", pizza_category="hammm")
        self.pizza4 = Pizzas.objects.create(
            pizza_name="peperoniiii", pizza_category="hammmm")

    def test_get_valid_single_pizza(self):
        response = client.get(
            reverse('get_delete_update_pizza', kwargs={'pk': self.pizza3.pk}))
        pizza = Pizzas.objects.get(pk=self.pizza3.pk)
        serializer = PizzasSerializer(pizza)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_pizza(self):
        response = client.get(
            reverse('get_delete_update_pizza', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateNewPizzaTest(TestCase):
    """ Testing to insert and create a new pizza """

    def setUp(self):
        self.valid_payload = {
            'pizza_name': 'pizza11',
            'pizza_category': 'ham'
        }
        self.invalid_payload = {
            'pizza_name': '',
            'pizza_category': 'ham',
        }

    def test_create_valid_pizza(self):
        response = client.post(
            reverse('get_post_pizzas'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_pizza(self):
        response = client.post(
            reverse('get_post_pizzas'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UpdateSinglePizzaTest(TestCase):
    """ Testing to update an existing pizza """

    def setUp(self):
        self.pizza1 = Pizzas.objects.create(
            pizza_name="peperoni", pizza_category="ham")
        self.pizza2 = Pizzas.objects.create(
            pizza_name="peperonii", pizza_category="hamm")
        self.valid_payload = {
            'pizza_name': 'pizza11',
            'pizza_category': 'ham'
        }
        self.invalid_payload = {
            'pizza_name': '',
            'pizza_category': 'ham',
        }

    def test_valid_update_pizza(self):
        response = client.put(
            reverse('get_delete_update_pizza', kwargs={'pk': self.pizza2.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_update_pizza(self):
        response = client.put(
            reverse('get_delete_update_pizza', kwargs={'pk': self.pizza2.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteSinglePizzaTest(TestCase):
    """ Testing to delete an existing piiza """

    def setUp(self):
        self.pizza1 = Pizzas.objects.create(
            pizza_name="peperoni", pizza_category="ham")
        self.pizza2 = Pizzas.objects.create(
            pizza_name="peperonii", pizza_category="hamm")

    def test_valid_delete_pizza(self):
        response = client.delete(
            reverse('get_delete_update_pizza', kwargs={'pk': self.pizza1.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_pizza(self):
        response = client.delete(
            reverse('get_delete_update_pizza', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
