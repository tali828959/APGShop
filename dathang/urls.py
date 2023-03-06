from django.urls import path
from . import views

app_name = 'dathang'

urlpatterns = [
    path('taodonhang/', views.taodonhang, name='taodonhang.html'),
    path('lichsu/', views.lichsumuahang, name='lichsumuahang.html'),
]
