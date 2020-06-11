from django.db import models

# Create your models here.
class Pizzas(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250, blank=True)
    category = models.CharField(max_length=250, blank=True)
    price = models.FloatField(blank=True)
    options = models.CharField(max_length=250, blank=True)
