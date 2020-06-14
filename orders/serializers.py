from rest_framework import serializers
from .models import Orders

#api representation
class OrdersSerializer(serializers.ModelSerializer):    
    """Serializer allow complex data to be converted to native Python in order to be rendered as JSON

    return:
        All the model field
    """
    class Meta:
        model = Orders
        fields = '__all__'