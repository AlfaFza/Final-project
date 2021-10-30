from django.urls import path
from . import views
from shop.models import *
from .models import *

urlpatterns = [

    path('cart_details',views.cart_details,name="cart_details"),
    path('add/<int:product_id>/',views.add_cart,name="add_cart"),
    path('cart_decrement/<int:product_id>/',views.min_cart,name="cart_decrement"),
    path('remove/<int:product_id>/',views.cart_delete,name="remove"),

]