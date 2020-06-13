from django.db import models
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
    pizza_list = models.TextField()

    def __str__(self):
        return self.id

    def set_pizza_list(self, x):
        self.pizza_list = json.dumps(x)

    def get_pizza_list(self):
        return json.loads(self.pizza_list)
