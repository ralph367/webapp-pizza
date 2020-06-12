from django.shortcuts import render
from rest_framework.views import APIView
from .models import Orders
from django.http import HttpResponse
from .serializers import OrdersSerializer
from rest_framework.response import Response
from rest_framework import status

class HomeView(APIView):
    template_name = 'orders.html'

    def get(self, request):
        orders = Orders.objects.all()
        return render(request, self.template_name, {'orders': orders, 'session_orders': request.session['order']})


def CartCheckout(request):
    cart = request.session.get('cart', [])
    delivery_charge = 3
    euro_rate = 1.13
    return render(request, 'checkout.html', {'cart': cart, 'delivery_charge': delivery_charge, 'euro_rate': euro_rate})

