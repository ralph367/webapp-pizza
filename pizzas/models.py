from django.db import models

# Create your models here.
class Pizzas(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250, blank=True)
    category = models.CharField(max_length=250, blank=True)
    price = models.CharField(max_length=250, blank=True)
    options = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.name

    def get_pizza(self):
        return self.name + ' in category ' + self.category