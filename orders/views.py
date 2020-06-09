from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Orders

class HomeView(TemplateView):
    template_name = 'orders.html'

    def get(self, request):
        orders = Orders.objects.all()
        return render(request, self.template_name, {'orders': orders})

    def post(self, request):
  
        return render(request, self.template_name, {})
