from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import OrdersSerializer
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import status
from .models import Orders
from pizzas.models import Pizzas
from pizzas.views import GetPizzasIDFromSession
from django.http import HttpResponse, HttpResponseRedirect
from pizzawebapp.variables import UNAVAILABE_PIZZA, DOLLAR, DOLLAR_RATE, DELIVERY_CHARGES


class OrdersViewSet(viewsets.ModelViewSet):
    queryset = Orders.objects.all().order_by('id')
    serializer_class = OrdersSerializer
    renderer_classes = [TemplateHTMLRenderer]

    def create(self, request):
        """Creating an order on request

        Args:
            request.cart (dict): cart session data
            request.currency (char): the wanted currency to pay with
            request.phone (char): phone number of the client
            request.location (char): location of the client
            request.addition_info (char): additional information from the client
            request.name (char): client name

        Returns:
            HttpResponse: 
                - 501: Unavailable pizza in the cart
            
            HttpResponseRedirect:
                - 200: redirect to orderlist when order is added
        """
        cart = request.session.get('cart', [])
        currency = request.data.get('currency')
        total_cost = 0
        pizzas_id_in_cart = GetPizzasIDFromSession(request)
        for pizza in cart:
            try:
                current_pizza = Pizzas.objects.get(id=pizza['id'])
                total_cost += pizza['amount'] * current_pizza.price
            except:
                return HttpResponse( UNAVAILABE_PIZZA, status=status.HTTP_501_NOT_IMPLEMENTED)
        total_cost += DELIVERY_CHARGES
        if currency == DOLLAR:
            total_cost = total_cost * DOLLAR_RATE
        data = {
            'price': total_cost,
            'currency': currency,
            'location': request.data.get('location'),
            'phone': request.data.get('phone'),
            'addition_info': request.data.get('addition_info'),
            'person_name': request.data.get('name'),
            'pizza_list': pizzas_id_in_cart,
        }
        serializer = OrdersSerializer(data=data)
        
        if serializer.is_valid():
            if ( not request.user.is_anonymous ):
                serializer.save(user=request.user)
            serializer.save()
            order = request.session.get('order', [])
            request.session['order'] = order
            temp_orders = request.session['order']
            temp_orders.append({'data': [data], 'cart': cart})
            request.session['order'] = temp_orders
            request.session['cart'] = []
            return Response({'session_orders': request.session['order']}, template_name="orders.html", status=status.HTTP_201_CREATED)
        return Response({}, template_name="orders.html", status=status.HTTP_406_NOT_ACCEPTABLE)