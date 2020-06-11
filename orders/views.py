from django.shortcuts import render
from rest_framework.views import APIView
from .models import Orders

class HomeView(APIView):
    template_name = 'orders.html'

    def get(self, request):
        orders = Orders.objects.all()
        return render(request, self.template_name, {'orders': orders})

    def post(self, request):
  
        return render(request, self.template_name, {})

def CartCheckout(request):
    cart = request.session.get('cart', [])
    return render(request, 'checkout.html', {'orders': cart})