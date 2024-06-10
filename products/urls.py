from django.urls import path
from .views import *
urlpatterns = [
    path('',all_products,name="home"),
    path('get_categories_response/<uuid:uuid>/',get_categories_response,name='get_categories_response'),
    path('get_product_view/<uuid:uuid>/',get_product_view,name="get_product_view"),
    path('view_cart/',view_cart,name="view_cart"),
    path('add_cart/<uuid:uuid>/',add_cart,name="add_cart")
]