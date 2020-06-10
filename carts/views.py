from django.shortcuts import render
from rest_framework.views import APIView
from .models import Carts
from pizzas.models import Pizzas
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseRedirect
from django.contrib import messages


class HomeView(APIView):
    template_name = 'carts.html'

    def get(self, request):
        carts = Carts.objects.all()
        return render(request, self.template_name, {'carts': carts})

    def post(self, request):

        return render(request, self.template_name, {})


def update_session(request):
    if not request.is_ajax() or not request.method == 'POST':
        return HttpResponseNotAllowed(['POST'])
    pizza_id = request.POST.get('id')
    pizza_amount = int(request.POST.get('amount'))
    temp_pizzas = request.session['cart']
    if (pizza_amount < 1):
        messages.add_message(request, messages.INFO, 'Hello world.')
        return HttpResponse("Negative amount", 300)
    my_item = next(
        (item for item in temp_pizzas if item['id'] == pizza_id), None)
    if (my_item is None):
        current_pizza = Pizzas.objects.get(id=pizza_id)
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

    print(request.session['cart'])
    return HttpResponse('Pizza successfully added', 200)
