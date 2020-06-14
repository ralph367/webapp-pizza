from django.shortcuts import render
from rest_framework.views import APIView
from .models import Orders
from .models import Pizzas
from django.http import HttpResponse
from .serializers import OrdersSerializer
from rest_framework.response import Response
from rest_framework import status
from pizzawebapp.variables import DELIVERY_CHARGES, DOLLAR_RATE


def GetSessionOrder( request):
    try:
        session_orders = request.session['order']
        return render(request, 'orders.html', { 'session_orders': session_orders})
    except:  
        return render(request, 'orders.html', { 'session_orders': []})


def CartCheckout(request):
    """Checkout html page to get the required info 

    Args:
        request.cart [dict]: all cart session items

    Returns:
        render: rendering to checkout.html page with the following data
            - 'cart': cart item data
            - 'delivery_charge': price of the delivery 
            - 'euro_rate': rate to transform from euro to dollar
    """
    cart = request.session.get('cart', [])
    return render(request, 'checkout.html', {'cart': cart, 'delivery_charge': DELIVERY_CHARGES, 'euro_rate': DOLLAR_RATE})

def OrdersHistory(request):
    """Getting the order histor of a user

    Args:
        request.user : who is the user that is requesting 

    Returns:
        render: rendering to history.html page with the following data
            - 'data': dict containing the pizza details from each order this user already made
    """
    pizzas = Pizzas.objects.all()
    data = []
    order_by_active_user = Orders.objects.filter(user=request.user)
    for order in order_by_active_user:
        data.append({'order': order, 'pizzas': order.pizza_list.all()})
    return render(request,'history.html',{'data': data})

