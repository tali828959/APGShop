
from django.db import models
from Computer.models import SANPHAM
# Create your models here.
class KHACHHANG(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=150)
    fullname = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)
    email = models.EmailField(unique=False)
    address = models.CharField(max_length=500, unique=False)

    def __str__(self):
        return self.username

# class DonHang(models.Model):
#     khachhang = models.ForeignKey(KHACHHANG,
#                               related_name='donhang_khachhang',
#                               on_delete=models.CASCADE)
#     ngaydathang = models.DateField()
#     httt = models.CharField(max_length=50)
#     diachigiaohang = models.CharField(max_length=250)
#     tongtien = models.FloatField()
#     tamung = models.FloatField()
#     conlai = models.FloatField()

#     def __str__(self):
#         return self.diachigiaohang

# class CTDonHang(models.Model):
#     donhang = models.ForeignKey(DonHang,
#                               related_name='donhang_items',
#                               on_delete=models.CASCADE)
#     sanpham = models.ForeignKey(SANPHAM,
#                                 related_name='sanpham_items',
#                                 on_delete=models.CASCADE)
#     gia = models.DecimalField(max_digits=10, decimal_places=2)
#     soluong = models.PositiveIntegerField(default=1)

#     def __str__(self):
#         return str(self.id)

#     def get_cost(self):
#         return self.gia * self.soluong
