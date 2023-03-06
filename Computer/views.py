from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from giohang.giohang import Giohang
from . import models
from . import forms
from django.db.models import Count, F, Value
import datetime
# Phân trang
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.
danhmuc = models.LOAISANPHAM.objects.all()
now = datetime.datetime.now()
ngaythangnam = str(now.day)+"/"+str(now.month)+"/"+str(now.year)
search_str = ''
subcategory = 0

def index(request):
    giohang = Giohang(request)
    ds_laptop_view = models.SANPHAM.objects.filter(ma_loai=1)
    ds_lap_banchay = ds_laptop_view.order_by("don_gia")[:4]
    ds_lap_noibat = ds_laptop_view.order_by("luot_xem")[:4]
    ds_pc_view = models.SANPHAM.objects.filter(ma_loai=2)
    ds_pc_banchay = ds_laptop_view.order_by("don_gia")[:4]
    ds_pc_noibat = ds_laptop_view.order_by("luot_xem")[:4]
    return render(request, "Computer/index.html", { 'danhmuc': danhmuc,'ds_banchay': ds_lap_banchay ,
                                                   'ds_noibat': ds_lap_noibat, 'ds_laptop_view': ds_laptop_view, 
                                                   'now': ngaythangnam, 'cart':giohang, 'ds_pc_banchay': ds_pc_banchay,
                                                   'ds_pc_noibat': ds_pc_noibat})

    # return render(request, "Computer/index.html")

def cart(request):
    return render(request, "Computer/cart.html")

def shop(request, pk):
    giohang = Giohang(request)
    product_list = []
    subcategory_name = ''
    if pk != 0:
        product_list = models.SANPHAM.objects.filter(ma_loai=pk).order_by("ngay_tao")
        selected_sub = models.LOAISANPHAM.objects.get(pk = pk)
        subcategory_name = selected_sub.ten_loai
    else:
        product_list = models.SANPHAM.objects.order_by("ngay_tao")

    page = request.GET.get('page', 1) # trang bat dau
    paginator = Paginator(product_list, 3) # so product/trang
    
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, "Computer/shop.html",
                    {'danhmuc': danhmuc,
                    'products': products,
                    'pk': pk,
                    'subcategory_name': subcategory_name, 'cart': giohang
                    })
    
    # return render(request, "Computer/shop.html")

def sanpham(request,pk):
    # cart = Cart(request)
    sanpham_select = models.SANPHAM.objects.get(pk=pk)
    models.SANPHAM.objects.filter(pk=sanpham_select.pk).update(luot_xem=F('luot_xem') + 1)
    sanpham_select.refresh_from_db()
    return render(request, "Computer/sanpham.html", {'sanpham': sanpham_select, 'danhmuc': danhmuc})

    # return render(request, "store/product.html", {'product': product_select, 'subcategories': subcategory_list, 'cart': cart})
    # return render(request, "Computer/sanpham.html")

def checkout(request):
    return render(request, "Computer/checkout.html")

def contact(request):
    giohang = Giohang(request)    
    result = '...'
    form = forms.FormLienhe()
    if request.method == 'POST':
        form = forms.FormLienhe(request.POST, models.Lienhe)
        if form.is_valid():
            request.POST_mutable = True
            post = form.save(commit=False)
            post.hoten = form.cleaned_data['hoten']
            post.sdt = form.cleaned_data['sdt']
            post.email = form.cleaned_data['email']
            post.chude = form.cleaned_data['chude']
            post.noidung = form.cleaned_data['noidung']
            post.save()
            result = 'Cám ơn quý khách đã liên hệ, chúng tôi sẽ hỗ trợ trong thời gian sớm nhất!'
        else:
            form= forms.FormLienhe()
    
    # return render(request, "stories/contact.html",
    #                         {'today':now, 'latest':latest, 'newest':newest_4, 'result': result, 'form': form})
    return render(request, "Computer/contact.html", {'giohang': giohang, 'danhmuc': danhmuc, 'result': result, 'form': form, 'now': ngaythangnam})
def tim_kiem(request):
    giohang = Giohang(request)
    username = request.session.get('username', 0)
    global danhmuc
    global search_str
    product_items = 0
   
    product_list = []
    if request.method == 'GET':
        # form = forms.Tim_Kiem(request.GET, models.SANPHAM)
        search_str = request.GET.get('name')
        if search_str != '':            
            product_list = models.SANPHAM.objects.filter(
                    ten_sp__contains=search_str).order_by("-ngay_tao")

        product_items = len(product_list)
        page = request.GET.get('page', 1)
        paginator = Paginator(product_list, 9)  # so product/trang

        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)

        return render(request, "Computer/shop.html",
                      {                       
                       'products': products,                       
                       'danhmuc': danhmuc,
                       'product_list': product_list,
                       'product_items': product_items,                       
                       'search_str': search_str,
                       'username': username,
                       'cart': giohang
                       })

