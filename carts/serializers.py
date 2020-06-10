from rest_framework import serializers
from .models import Carts

#api representation
class CartsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carts
        fields = '__all__'