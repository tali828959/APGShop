# Generated by Django 4.1.3 on 2023-03-02 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('khachhang', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donhang',
            name='khachhang',
        ),
        migrations.DeleteModel(
            name='CTDonHang',
        ),
        migrations.DeleteModel(
            name='DonHang',
        ),
    ]
