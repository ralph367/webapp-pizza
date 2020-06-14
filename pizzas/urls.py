from django.urls import include, path
from rest_framework import routers
from . import viewsets
from . import views
from django.conf.urls import url

router = routers.DefaultRouter()
# routing all the pizzas viewset functions
router.register(r'pizzas', viewsets.PizzasViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework_pizzas')),
    path('', views.HomeView.as_view(), name='home'),
    path('addtocartsession', views.add_cart_session, name='addtocart'),
    path('updatecartsession', views.update_cart_session, name='updatecart'),
    path('gettotalcost', views.cart_total_cost, name='totalcost'),
    path('clearcart', views.clear_cart, name='cartclear')
]