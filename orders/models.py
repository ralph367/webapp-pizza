from django.db import models
from django.contrib.auth.models import User
from pizzas.models import Pizzas
import json

# Create your models here.
class Orders(models.Model):
    id = models.AutoField(primary_key=True)
    price = models.CharField(max_length=250, blank=True)
    currency = models.CharField(max_length=250, blank=True)
    location = models.CharField(max_length=250, blank=True)
    phone = models.CharField(max_length=250, blank=True)
    addition_info = models.CharField(max_length=250, blank=True)
    person_name = models.CharField(max_length=250, blank=True)
    pizza_list = models.ManyToManyField(Pizzas)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="job", null=True)



