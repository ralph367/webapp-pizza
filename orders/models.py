from django.db import models

# Create your models here.
class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_price = models.CharField(max_length=250, blank=True)
    order_location = models.CharField(max_length=250, blank=True)
    order_phone = models.CharField(max_length=250, blank=True)
    order_addition_info = models.CharField(max_length=250, blank=True)
    order_person_name = models.CharField(max_length=250, blank=True)
    order_cart_id = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.order_id
