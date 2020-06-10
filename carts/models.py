from django.db import models

# Create your models here.
class Carts(models.Model):
    id = models.AutoField(primary_key=True)
    price = models.CharField(max_length=250, blank=True)
    pizzas_id = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.id