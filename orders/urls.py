from django.urls import include, path
from rest_framework import routers
from . import viewsets
from . import views
from django.conf.urls import url
from django.contrib.auth.decorators import login_required

router = routers.DefaultRouter()
# routing all the orders viewset functions
router.register(r'orders', viewsets.OrdersViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework_orders')),
    path('orderlist', views.HomeView.as_view(), name='orderlist'),
    path('checkout', views.CartCheckout, name='cartcheckout'),
    path('history', login_required(views.OrdersHistory), name='history')
]