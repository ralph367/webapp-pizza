from rest_framework import serializers
from .models import Orders

#api representation
class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'