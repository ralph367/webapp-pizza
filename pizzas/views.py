from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from .models import Pizzas
from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse
from pizzawebapp.variables import WRONG_VALUES, NEAGATIVE_AMOUNT, UNAVAILABE_PIZZA, SUCCESSFULLY_ADDED, EMPTY_CART, CLEARED_CART, SUCCESSFULLY_UPDATED
# Create your views here.


class HomeView(APIView):
    template_name = 'index.html'

    def get(self, request):
        pizzas = Pizzas.objects.all()
        return render(request, self.template_name, {'pizzas': pizzas})

    def post(self, request):
        return render(request, self.template_name, {})


def add_cart_session(request):
    """Creating cart session on pizza add to cart action

    Args:
        request.id (int): pizza id of the added pizza to the cart
        request.amout (int): quantity of the added pizza

    Returns:
        HttpResponse: 
            - 405: Not allowed if it isn't a post request
            - 417: Wrong values as arguments, not integers
            - 406: Negative values for amount arg, can't add -1 pizza
            - 501: Unavailable pizza, trying to add a pizza in the cart that isn't avaiable in our db
            - 200: Successfully added to the cart
    """
    if not request.method == 'POST':
        return HttpResponseNotAllowed(['POST'])
    cart = request.session.get('cart', [])
    request.session['cart'] = cart
    try:
        pizza_id = int(request.POST.get('id'))
        pizza_amount = int(request.POST.get('amount'))
    except:
        return HttpResponse(WRONG_VALUES, status=status.HTTP_417_EXPECTATION_FAILED)
    temp_pizzas = request.session['cart']
    if (pizza_amount < 1):
        return HttpResponse(NEAGATIVE_AMOUNT, status=status.HTTP_406_NOT_ACCEPTABLE)
    my_item = next(
        (item for item in temp_pizzas if item['id'] == pizza_id), None)
    if (my_item is None):
        try:
            current_pizza = Pizzas.objects.get(id=pizza_id)
        except:
            return HttpResponse(UNAVAILABE_PIZZA, status=status.HTTP_501_NOT_IMPLEMENTED)
        temp_pizzas.append({'id': pizza_id,
                            'amount': pizza_amount,
                            'description': current_pizza.description,
                            'name': current_pizza.name,
                            'price': current_pizza.price})
    else:
        temp_pizzas.remove(my_item)
        my_item['amount'] += pizza_amount
        temp_pizzas.append(my_item)
    pizza = Pizzas.objects.get(id=pizza_id)
    request.session['cart'] = temp_pizzas
    return HttpResponse(str(pizza.name)+" "+SUCCESSFULLY_ADDED, status=status.HTTP_200_OK)


def update_cart_session(request):
    """Updating the cart 

    Args:
        request.id (int): pizza id of the added pizza to the cart
        request.amout (int): quantity of the added pizza

    Returns:
        HttpResponse: 
            - 405: Not allowed if it isn't a post request
            - 412: Trying to update an empty cart
            - 417: Wrong values as arguments, not integers
            - 406: Negative values for amount arg, can't reach -1 pizza
            - 501: Unavailable pizza, trying to add a pizza in the cart that isn't avaiable in our db
            - 200: Successfully updated
    """
    if not request.method == 'POST':
        return HttpResponseNotAllowed(['POST'])
    cart = request.session.get('cart', [])
    if not cart:
        return HttpResponse(EMPTY_CART, status=status.HTTP_412_PRECONDITION_FAILED)
    try:
        pizza_id = int(request.POST.get('id'))
        pizza_amount = int(request.POST.get('amount'))
    except:
        return HttpResponse(WRONG_VALUES, status=status.HTTP_417_EXPECTATION_FAILED)
    temp_pizzas = request.session['cart']
    if (pizza_amount < 0):
        return HttpResponse(NEAGATIVE_AMOUNT, status=status.HTTP_406_NOT_ACCEPTABLE)
    my_item = next(
        (item for item in temp_pizzas if item['id'] == pizza_id), None)
    if (my_item is None):
        return HttpResponse(UNAVAILABE_PIZZA, status=status.HTTP_501_NOT_IMPLEMENTED)
    else:
        temp_pizzas.remove(my_item)
        my_item['amount'] = pizza_amount
        temp_pizzas.append(my_item)
    pizza = Pizzas.objects.get(id=pizza_id)
    request.session['cart'] = temp_pizzas
    return HttpResponse(str(pizza.name)+" "+SUCCESSFULLY_UPDATED, status=status.HTTP_200_OK)


def cart_total_cost(request):
    """Calculating the total cost of a cart

    Args:
        request.session (dict): cart session list of added the added items

    Returns:
        HttpResponse: 
            - 405: Not allowed if it isn't a get request
            - 501: Unavailable pizza, trying to calculate the cost wiht a pizza in the cart that isn't avaiable in our db

        JsonResponse: 
            - 200: total cost of the cart
    """
    if not request.method == 'GET':
        return HttpResponseNotAllowed(['GET'])
    cart = request.session.get('cart', [])
    if not cart:
        return JsonResponse({'total_cost': 0, 'cart': []}, status=status.HTTP_200_OK)
    total_cost = 0
    for pizza in cart:
        try:
            current_pizza = Pizzas.objects.get(id=pizza['id'])
            total_cost += pizza['amount'] * current_pizza.price
        except:
            return HttpResponse(UNAVAILABE_PIZZA, status=status.HTTP_501_NOT_IMPLEMENTED)
    return JsonResponse({'total_cost': total_cost, 'cart': cart}, status=status.HTTP_200_OK)


def clear_cart(request):
    """Clearing the cart/clearing the session

    Returns:
        HttpResponse:
            - 405: Not delete request
            - 200: cart cleared
    """
    if not request.method == 'DELETE':
        return HttpResponseNotAllowed(['DELETE'])
    request.session['cart'] = []
    return HttpResponse(CLEARED_CART, status=status.HTTP_200_OK)


def GetPizzasIDFromSession(request):
    """Get the pizzas ID from the cart session

    Args:
        request.cart (dict): cart list of the added items

    Returns:
        dict: dictonary showing the list of the pizzas id
    """
    cart = request.session.get('cart', [])
    pizzas = Pizzas.objects.all().values_list('id', flat=True)
    pizzasID = []
    for pizza in cart:
        if pizza['id'] in pizzas:
            pizzasID.append(pizza['id'])
    return pizzasID