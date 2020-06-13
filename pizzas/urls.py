from django.urls import include, path
from rest_framework import routers
from . import viewsets
from . import views
from django.conf.urls import url

router = routers.DefaultRouter()
router.register(r'pizzas', viewsets.PizzasViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework_pizzas')),
    path('pizzaslist', views.HomeView.as_view(), name='home'),
    path('addtocartsession', views.add_cart_session, name='addtocart'),
    path('updatecartsession', views.update_cart_session, name='updatecart'),
    path('gettotalcost', views.cart_total_cost, name='totalcost'),
    path('clearcart', views.clear_cart, name='cartclear')
    # url(
    #     r'^api/v1/pizzas/(?P<pk>[0-9]+)$',
    #     views.get_delete_update_pizza,
    #     name='get_delete_update_pizza'
    # ),
    # url(
    #     r'^api/v1/pizzas/$',
    #     views.get_post_pizzas,
    #     name='get_post_pizzas'
    # )
]