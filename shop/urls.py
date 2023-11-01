from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('buy/<int:product_id>/', views.PurchaseCreate.as_view(), name='buy'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('add_in_cart/<int:product_id>/', views.add_in_cart, name='add_in_cart'),
    path('delete_in_cart/<int:product_id>/', views.delete_in_cart, name='delete_in_cart'),
    path('delete_from_cart/<int:product_id>/', views.delete_from_cart, name='delete_from_cart'),
    path('cart/', views.cart_detail, name='cart_detail'),
]
