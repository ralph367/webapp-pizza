from django.db import models

# Create your models here.
class Orders(models.Model):
    id = models.AutoField(primary_key=True)
    price = models.CharField(max_length=250, blank=True)
    location = models.CharField(max_length=250, blank=True)
    phone = models.CharField(max_length=250, blank=True)
    addition_info = models.CharField(max_length=250, blank=True)
    person_name = models.CharField(max_length=250, blank=True)
    cart_id = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.id
