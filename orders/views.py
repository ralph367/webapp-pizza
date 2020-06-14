from django.shortcuts import render
from rest_framework.views import APIView
from .models import Orders
from .models import Pizzas
from django.http import HttpResponse
from .serializers import OrdersSerializer
from rest_framework.response import Response
from rest_framework import status

class HomeView(APIView):
    template_name = 'orders.html'

    def get(self, request):
        orders = Orders.objects.all()
        try:
            session_orders = request.session['order']

            return render(request, self.template_name, {'orders': orders, 'session_orders': session_orders})
        except:  
            return render(request, self.template_name, {'orders': orders, 'session_orders': []})


def CartCheckout(request):
    cart = request.session.get('cart', [])
    delivery_charge = 3
    euro_rate = 1.13
    return render(request, 'checkout.html', {'cart': cart, 'delivery_charge': delivery_charge, 'euro_rate': euro_rate})

def OrdersHistory(request):
    pizzas = Pizzas.objects.all()
    data = []
    order_by_active_user = Orders.objects.filter(user=request.user)
    for order in order_by_active_user:
        data.append({'order': order, 'pizzas': order.pizza_list.all()})
    return render(request,'history.html',{'data': data})

