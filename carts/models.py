from django.db import models

# Create your models here.
class Carts(models.Model):
    cart_id = models.AutoField(primary_key=True)
    cart_price = models.CharField(max_length=250, blank=True)
    cart_pizzas_id = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.cart_id