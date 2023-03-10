# Generated by Django 4.1.3 on 2023-02-21 07:30

import ckeditor_uploader.fields
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KHACHHANG',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ten_kh', models.CharField(max_length=250)),
                ('ngay_sinh', models.DateField()),
                ('dia_chi', models.CharField(max_length=500)),
                ('dien_thoai', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('mat_khau', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='LOAISANPHAM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ten_loai', models.CharField(max_length=250)),
                ('mo_ta', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('hinh_anh', models.ImageField(default='Computer/images/default.png', upload_to='Computer/images')),
            ],
        ),
        migrations.CreateModel(
            name='SANPHAM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ten_sp', models.CharField(max_length=250)),
                ('mota_tomtat', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('mota_chitiet', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('don_gia', models.FloatField(null=True)),
                ('hinh_anh', models.ImageField(default='Computer/images/default.png', upload_to='Computer/images')),
                ('luot_xem', models.IntegerField(default=0)),
                ('ngay_tao', models.DateTimeField(default=datetime.datetime.now)),
                ('ma_loai', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Computer.loaisanpham')),
            ],
        ),
    ]
