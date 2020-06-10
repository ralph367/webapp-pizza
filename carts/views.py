from django.shortcuts import render
from rest_framework.views import APIView
from .models import Carts

class HomeView(APIView):
    template_name = 'carts.html'

    def get(self, request):
        carts = Carts.objects.all()
        return render(request, self.template_name, {'carts': carts})

    def post(self, request):
  
        return render(request, self.template_name, {})

