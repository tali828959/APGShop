from django.db import models
import datetime
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User


# Create your models here.

    
class LOAISANPHAM(models.Model):
    # ma_loai, ten_loai, mo_ta, hinh_anh
    ten_loai = models.CharField(max_length=250)
    mo_ta = RichTextUploadingField(blank=True, null=True)
    hinh_anh = models.ImageField(upload_to="Computer/images",
                              default="Computer/images/default.png")
    def __str__(self):
        return self.ten_loai
    
class SANPHAM(models.Model):
    # ma_sp, ten_sp, ma_loai, mota_tomtat, mota_chitiet, don_gia, hinh_anh, so_lan_xem, ngay_tao
    ma_loai = models.ForeignKey(LOAISANPHAM, on_delete=models.PROTECT)
    ten_sp = models.CharField(max_length=250)
    mota_tomtat = RichTextUploadingField(blank=True, null=True)
    mota_chitiet = RichTextUploadingField(blank=True, null=True)
    don_gia = models.FloatField(null=True)
    hinh_anh = models.ImageField(upload_to="Computer/images",
                              default="Computer/images/default.png")
    luot_xem = models.IntegerField(default=0)    
    ngay_tao = models.DateTimeField(default=datetime.datetime.now)
    
    def __str__(self):
        return self.ten_sp
    
class KHACHHANG(models.Model):
    username = models.CharField(max_length=250, unique=True)
    password = models.CharField(max_length=250)
    confirm = models.CharField(max_length=250)
    fullname = models.CharField(max_length=250)
    phone = models.CharField(max_length=20, null=True)
    email =  models.EmailField()
    address = models.CharField(max_length=250)

    def __str__(self):
        return self.username
    
class Lienhe(models.Model):
    hoten = models.CharField(max_length=250)
    email = models.EmailField()
    sdt = models.CharField(max_length=20, null=True)
    chude = models.CharField(max_length=264)
    noidung = models.TextField()

    def __str__(self):
        return self.hoten + ", " + self.chude
