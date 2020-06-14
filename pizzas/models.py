from django.db import models

# Create your models here.
class Pizzas(models.Model):
    """Pizza models that will be saved in mysql 

    Args:
        id (int): Primary key of the Pizza model
        name (char): Pizza name 
        description (char): Pizza components
        category (char): Not implemented yet
        price (float): Pizza cost in euro
        options (char): Not implemenet yet
        image (text): Image name that will be uploaded to django's media file
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250, blank=True)
    category = models.CharField(max_length=250, blank=True)
    price = models.FloatField(blank=True)
    options = models.CharField(max_length=250, blank=True)
    image = models.ImageField(upload_to='images/', blank=True)

    def get_name(self):
        return self.name