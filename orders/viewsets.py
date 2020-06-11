from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import OrdersSerializer
from rest_framework import status
from .models import Orders
from django.http import HttpResponse


class OrdersViewSet(viewsets.ModelViewSet):
    queryset = Orders.objects.all().order_by('id')
    serializer_class = OrdersSerializer

    def create(self, request):
        cart = request.session.get('cart', [])
        data = {
            'price': '1',
            'location': request.data.get('location'),
            'phone': request.data.get('phone'),
            'addition_info': request.data.get('addition_info'),
            'person_name': request.data.get('name'),
            'pizza_list': str(cart)
        }
        serializer = OrdersSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
