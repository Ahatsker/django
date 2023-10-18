from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_detail, name='carts_detail'),
    path('add/<int:product_id>/', views.cart_add, name='carts_add'),
    path('remove/<int:product_id>/', views.cart_remove, name='carts_remove'),
    path('buy/', views.buy, name='carts_buy')
]
