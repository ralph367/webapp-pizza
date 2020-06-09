from django.db import models

# Create your models here.
class Pizzas(models.Model):
    pizza_id = models.AutoField(primary_key=True)
    pizza_name = models.CharField(max_length=250)
    pizza_description = models.CharField(max_length=250, blank=True)
    pizza_category = models.CharField(max_length=250, blank=True)
    pizza_price = models.CharField(max_length=250, blank=True)
    pizza_options = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.pizza_name

    def get_pizza(self):
        return self.pizza_name + ' in category ' + self.pizza_category