from django.shortcuts import render
from pizzas.models import Pizzas
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import PizzasSerializer
from django.http import HttpRequest
# Create your views here.


def index(response):
    fake_request = HttpRequest()
    fake_request.method = 'GET'
    pizzas = get_post_pizzas(fake_request)
    return render(response, "index.html", {'pizzas': pizzas.data})


@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_pizza(request, pk):
    try:
        pizza = Pizzas.objects.get(pk=pk)
    except Pizzas.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get single pizza
    if request.method == 'GET':
        serializer = PizzasSerializer(pizza)
        return Response(serializer.data)
    # delete one pizza
    elif request.method == 'DELETE':
        pizza.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    # update a pizza
    elif request.method == 'PUT':
        serializer = PizzasSerializer(pizza, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def get_post_pizzas(request):
    # get all pizzas
    if request.method == 'GET':
        pizzas = Pizzas.objects.all()
        serializer = PizzasSerializer(pizzas, many=True)
        return Response(serializer.data)
    # insert a pizza in the table
    elif request.method == 'POST':
        data = {
            'pizza_name': request.data.get('pizza_name'),
            'pizza_category': request.data.get('pizza_category')
        }
        serializer = PizzasSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
