from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from Computer.models import SANPHAM
from .giohang import Giohang
from .forms import CartAddProductForm


@require_POST
def cart_add(request, product_id):
    cart = Giohang(request)
    id=request.session.get('idkh', False)
    if id==False:
        return redirect("khachhang:dangnhap.html")
        
    product = get_object_or_404(SANPHAM, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 override_quantity=cd['override'])
    return redirect('giohang:cart_detail')


@require_POST
def cart_remove(request, product_id):
    cart = Giohang(request)
    product = get_object_or_404(SANPHAM, id=product_id)
    cart.remove(product)
    return redirect('giohang:cart_detail')


def cart_detail(request):
    cart = Giohang(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'],
                                                                   'override': True})
    return render(request, 'giohang/giohang.html', {'cart': cart})
