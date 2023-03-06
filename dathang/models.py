from django.db import models

# Create your models here.

from Computer.models import SANPHAM


class Order(models.Model):
    username = models.CharField(max_length=50, null=True)
    full_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20, null=True)
    address = models.CharField(max_length=500, unique=False)
    ngaytao = models.DateTimeField(auto_now_add=True)
    ngaycapnhat = models.DateTimeField(auto_now=True)
    thanh_toan = models.BooleanField(default=False)

    class Meta:
        ordering = ('-ngaytao',)

    def __str__(self):
        return f'Order {self.id}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order,
                              related_name='items',
                              on_delete=models.CASCADE)
    product = models.ForeignKey(SANPHAM,
                                related_name='order_items',
                                on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity


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
