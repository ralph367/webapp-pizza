from django.db import models
from django.contrib.auth.models import User
from pizzas.models import Pizzas
import json

# Create your models here.
class Orders(models.Model):
    """Order models that will be saved in mysql 

    Args:
        id (int): Primary key of the Order model
        price (char): Total order price saved in the model
        currency (char): Euro or Dollar, the order is paid with which currency
        location (char): Location to deliver the order to
        phone (char): Phone number to contact the client
        addition_info (char): An additional field for the client 
        person_name (char): The cliend name
        pizza_list (int): a list of the pizzas, a new db table will be created showing the order ID and the pizza ID
        user (int): if a logged in user made a requst his account id will be saved in the order model
    """
    id = models.AutoField(primary_key=True)
    price = models.CharField(max_length=250, blank=True)
    currency = models.CharField(max_length=250, blank=True)
    location = models.CharField(max_length=250, blank=True)
    phone = models.CharField(max_length=250, blank=True)
    addition_info = models.CharField(max_length=250, blank=True)
    person_name = models.CharField(max_length=250, blank=True)
    pizza_list = models.ManyToManyField(Pizzas)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="job", null=True)



