from django.urls import path
from . import views

app_name = 'Computer'
urlpatterns = [
    path('', views.index, name='index.html'),
    path('index.html', views.index, name='index.html'),
    path('cart.html', views.cart, name='cart.html'),
    path('checkout.html', views.checkout, name='checkout.html'),
    path('contact.html', views.contact, name='contact.html'),
    path('sanpham.html/<int:pk>/', views.sanpham, name='sanpham.html'),
    path('shop.html/<int:pk>/', views.shop, name='shop.html'),
    path('search.html', views.tim_kiem, name='search.html'),
]