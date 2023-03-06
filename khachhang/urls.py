from django.urls import path
from . import views

app_name = 'khachhang'
urlpatterns = [
    path('', views.index, name='index.html'),
    path('dangky.html', views.dang_ky, name='dangky.html'),
    path('dangnhap.html', views.dang_nhap, name='dangnhap.html'),
    path('dangxuat.html', views.dang_xuat, name='dangxuat.html'),
    # path('dathang.html', views.dat_hang, name='dathang.html'),
]