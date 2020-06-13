from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import OrdersSerializer
from rest_framework import status
from .models import Orders
from pizzas.models import Pizzas
from django.http import HttpResponse


class OrdersViewSet(viewsets.ModelViewSet):
    queryset = Orders.objects.all().order_by('id')
    serializer_class = OrdersSerializer

    def create(self, request):
        cart = request.session.get('cart', [])
        currency = request.data.get('currency')
        total_cost = 0
        for pizza in cart:
            try:
                current_pizza = Pizzas.objects.get(id=pizza['id'])
                total_cost += pizza['amount'] * current_pizza.price
            except:
                return HttpResponse("Unavailable Pizza", status=501)
        total_cost += 3
        if currency == 'dolar':
            total_cost = total_cost * 1.13
        data = {
            'price': total_cost,
            'currency': currency,
            'location': request.data.get('location'),
            'phone': request.data.get('phone'),
            'addition_info': request.data.get('addition_info'),
            'person_name': request.data.get('name'),
            'pizza_list': cart
        }
        serializer = OrdersSerializer(data=data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            order = request.session.get('order', [])
            request.session['order'] = order
            temp_orders = request.session['order']
            temp_orders.append(serializer.data)
            request.session['order'] = temp_orders
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
