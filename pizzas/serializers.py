from rest_framework import serializers
from .models import Pizzas

#api representation
class PizzasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizzas
        fields = '__all__'