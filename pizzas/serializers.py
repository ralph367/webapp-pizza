from rest_framework import serializers
from .models import Pizzas

# api representation


class PizzasSerializer(serializers.ModelSerializer):
    """Serializer allow complex data to be converted to native Python in order to be rendered as JSON
    """
    class Meta:
        model = Pizzas
        fields = '__all__'
