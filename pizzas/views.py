from django.shortcuts import render
from rest_framework.views import APIView
from .models import Pizzas
# Create your views here.

class HomeView(APIView):
    template_name = 'index.html'

    def get(self, request):
        pizzas = Pizzas.objects.all()
        return render(request, self.template_name, {'pizzas': pizzas, 'request': request})

    def post(self, request):
        return render(request, self.template_name, {})
