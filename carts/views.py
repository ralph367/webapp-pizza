from django.shortcuts import render
from rest_framework.views import APIView
from .models import Carts
from pizzas.models import Pizzas
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseRedirect


class HomeView(APIView):
    template_name = 'carts.html'

    def get(self, request):
        carts = Carts.objects.all()
        return render(request, self.template_name, {'carts': carts})

    def post(self, request):

        return render(request, self.template_name, {})


def add_cart_session(request):
    if not request.method == 'POST':
        return HttpResponseNotAllowed(['POST'])
    cart = request.session.get('cart', [])
    request.session['cart'] = cart
    try:
        pizza_id = int(request.POST.get('id'))
        pizza_amount = int(request.POST.get('amount'))
    except:
        return HttpResponse("Wrong Values", status=417)
    temp_pizzas = request.session['cart']
    if (pizza_amount < 1):
        return HttpResponse("Negative amount", status=406)
    my_item = next(
        (item for item in temp_pizzas if item['id'] == pizza_id), None)
    if (my_item is None):
        try:
            current_pizza = Pizzas.objects.get(id=pizza_id)
        except:
            return HttpResponse("Unnavailable Pizza", status=501)
        temp_pizzas.append({'id': pizza_id,
                            'amount': pizza_amount,
                            'description': current_pizza.description,
                            'name': current_pizza.name,
                            'price': current_pizza.price})
    else:
        temp_pizzas.remove(my_item)
        my_item['amount'] += pizza_amount
        temp_pizzas.append(my_item)

    request.session['cart'] = temp_pizzas
    return HttpResponse('Pizza successfully added', status=200)


def update_cart_session(request):
    if not request.method == 'POST':
        return HttpResponseNotAllowed(['POST'])
    cart = request.session.get('cart', [])
    if not cart:
        return HttpResponse("Cart is empty you can't udpate", status=412)
    try:
        pizza_id = int(request.POST.get('id'))
        pizza_amount = int(request.POST.get('amount'))
    except:
        return HttpResponse("Wrong Values", status=417)
    temp_pizzas = request.session['cart']
    if (pizza_amount < 1):
        return HttpResponse("Negative amount", status=406)
    my_item = next(
        (item for item in temp_pizzas if item['id'] == pizza_id), None)
    if (my_item is None):
        return HttpResponse("Can't update an unavailable pizza", status=501)
    else:
        temp_pizzas.remove(my_item)
        my_item['amount'] = pizza_amount
        temp_pizzas.append(my_item)

    request.session['cart'] = temp_pizzas
    return HttpResponse('Pizza successfully update', status=200)