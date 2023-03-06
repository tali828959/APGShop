from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import make_password, check_password
from .forms import FormKHACHHANG
from .models import KHACHHANG
from django.shortcuts import redirect
from Computer import models
from datetime import datetime
from giohang.giohang import Giohang
# thư viện cho việc sử dụng email
from ShopOnlineComputer.settings import EMAIL_HOST_USER
from django.core.mail import send_mail

from django.core.mail import EmailMultiAlternatives

# Create your views here.

def index(request):
    return render(request, "khachhang/index.html")

def dang_ky(request):
    # giohang = Giohang(request)
    if request.method == "POST":
        form = FormKHACHHANG(data=request.POST)
        if (form.is_valid() and form.cleaned_data['password'] == form.cleaned_data['confirm']):            
            kh = form.save(commit=False)
            kh.password = make_password(kh.password)
            print(kh.password)
            print(kh.save())
            # Gửi email
            email_address = kh.email
            subject = 'Chúc mừng quý khách đăng ký tài khoản thành công tại trang web T3h Shop Online'
            message = 'Cảm ơn quý khách <b>'+ kh.fullname +'</b> đã đăng ký tại T3h Shop Onl,'
            recepient = str(email_address)
            html_content = '''
            <p style="margin:4px 0;font-family:Arial, Helvetica, sans-serif;font-size:12px;color:#444;line-height:18px;font-weight:normal;">My Store rất vui thông báo tới Quý Khách ''' + \
                ''' quá trình tạo tài khoản đã thành công. </p>									
			<h3 style="font-size:13px;font-weight:bold;color:#02acea;text-transform:uppercase;margin:20px 0 0 0;border-bottom:1px solid #ddd;">Thông tin tài khoản:</h3>''' + \
                '''<h5>Họ và tên: ''' + \
                kh.fullname + \
                ''' ''' + \
                '''</h5> ''' + \
                '<h5>Phone: ' + \
                str(kh.phone) + \
                '''</h5><h5>Địa chỉ giao hàng: ''' + \
                kh.address + \
                '''</h5><h5>Email nhận thông tin: ''' + \
                kh.email + \
                '''</h5> '''
            msg = EmailMultiAlternatives(subject, message, EMAIL_HOST_USER, [recepient])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            result = "Tạo tài khoản thành công"
            # return render(request, 'khachhang/dangky.html',{'form': form, 'Giohang': giohang, 'result': result})
            return render(request, 'khachhang/dangky.html',{'form': form, 'result': result})
    else:
        form = FormKHACHHANG()
    username = request.session.get('username', 0)
    # return render(request, 'khachhang/dangky.html',{'form': form, 'Giohang': giohang})
    return render(request, 'khachhang/dangky.html',{'form': form, })

def dang_nhap(request):
    giohang = Giohang(request)
    if request.method == "POST":
        _username = request.POST.get("username")
        _password = request.POST.get("password")
        kh = KHACHHANG.objects.get(username =_username)
        if kh is not None:  
            checkpassword=check_password(_password, kh.password)    
            if check_password:      
                request.session['kh'] = kh.fullname
                request.session['idkh'] = kh.id
                return redirect("Computer:index.html")
            else:
                print("Username: {} and password: {}".format(_username, _password))
                login_result = "Username hoặc password không chính xác!"
                return render(request, "khachhang/dangnhap.html", {'login_result': login_result, 'giohang': giohang})
        else:
            print("Username: {} and password: {}".format(_username, _password))
            login_result = "Username hoặc password không chính xác!"
            return render(request, "khachhang/dangnhap.html", {'login_result': login_result, 'giohang': giohang})
    else:
        return render(request, "khachhang/dangnhap.html", { 'giohang': giohang})

def dang_xuat(request):
    giohang = Giohang(request)
    giohang.clear()    
    del request.session['kh']
    del request.session['idkh']
    return redirect("Computer:index.html")

# def dat_hang(request):
#     giohang = Giohang(request)
#     id=request.session.get('idkh', False)
#     form = FormDonHang()
#     if id==False:
#         return redirect("khachhang:dangnhap.html")
#     kh = KHACHHANG.objects.get(pk = id)
#     if request.method == "POST":
#         dh = DonHang.objects.create(khachhang=kh,
#                                          ngaydathang=datetime.now(),
#                                          httt=request.POST.get("httt"),
#                                          diachigiaohang=request.POST.get("diachigiaohang"),
#                                          tongtien=0,tamung=0,conlai=0)
#         giohang = Giohang(request)
#         for item in giohang:
#                 CTDonHang.objects.create(donhang=dh,
#                                          sanpham=item['product'],
#                                          gia=item['price'],
#                                          soluong=item['quantity'])
#         # Gửi email
#         email_address = kh.email
#         subject = 'Xác nhận đơn hàng ' + str(dh.id)
#         message = 'Cảm ơn quý khách <b>' +' ' + kh.fullname + '</b> đã đặt hàng tại T3h Shop Online,'
#         recepient = str(email_address)

#         html_content = '''
#         <p style="margin:4px 0;font-family:Arial, Helvetica, sans-serif;font-size:12px;color:#444;line-height:18px;font-weight:normal;">My Store rất vui thông báo đơn hàng ''' + \
#         str(dh.id) + \
#         ''' của quý khách đã được tiếp nhận và đang trong quá trình xử lý. </p>									
#         <h3 style="font-size:13px;font-weight:bold;color:#02acea;text-transform:uppercase;margin:20px 0 0 0;border-bottom:1px solid #ddd;">Thông tin đơn hàng:</h3>''' + \
#         '''<h5>Họ và tên: ''' + \
#         kh.fullname + \
#         '''</h5> ''' + \
#         '<h5>Phone: ' + \
#         str(kh.phone) + \
#         '''</h5><h5>Địa chỉ giao hàng: ''' + \
#         dh.diachigiaohang + \
#         '''</h5> ''' + \
#         '''<h2 style="text-align:left;margin:10px 0;border-bottom:1px solid #ddd;padding-bottom:5px;font-size:13px;color:#02acea;">CHI TIẾT ĐƠN HÀNG</h2>''' + \
#         '''<table border="0" cellpadding="0" cellspacing="0" style="background:#f5f5f5;" width="100%">''' + \
#         ''' <thead>
#                                         <tr>
#                                             <th align="left" bgcolor="#02acea" style="padding:6px 9px;color:#fff;font-family:Arial, Helvetica, sans-serif;font-size:12px;line-height:14px;">Sản phẩm</th>
#                                             <th align="left" bgcolor="#02acea" style="padding:6px 9px;color:#fff;font-family:Arial, Helvetica, sans-serif;font-size:12px;line-height:14px;">Đơn giá</th>
#                                             <th align="left" bgcolor="#02acea" style="padding:6px 9px;color:#fff;font-family:Arial, Helvetica, sans-serif;font-size:12px;line-height:14px;">Số lượng</th>
#                                             <th align="right" bgcolor="#02acea" style="padding:6px 9px;color:#fff;font-family:Arial, Helvetica, sans-serif;font-size:12px;line-height:14px;">Tổng tạm</th>
#                                         </tr>
#                                     </thead>
#                                     <tbody style="font-family:Arial, Helvetica, sans-serif;font-size:12px;color:#444;line-height:18px;">
#         '''
#         for item in giohang:
#             html_content += '''
#             <tr>
#                 <td align="left" style="padding:3px 9px;" valign="top"><span class="yiv1530170030name">''' + \
#                 str(item['product']) + \
#                 '''</td>''' + \
#                 '''<td align="left" style="padding:3px 9px;" valign="top"><span>''' + \
#                 str("{:0,.0f}".format(float(item['price']))) + \
#                 '''</span></td>''' + \
#                 ''' <td align="left" style="padding:3px 9px;" valign="top">''' + \
#                 str(item['quantity']) + \
#                 '''</td>''' + \
#                 '''<td align="right" style="padding:3px 9px;" valign="top"><span>''' + \
#                 str("{:0,.0f}".format(item['total_price'])) + \
#                 '''</span></td></tr>'''
#         html_content += '''<tr><td colspan="4" style="text-align:right">Tổng đơn hàng:''' + \
#             str("{:0,.0f}".format(giohang.get_total_price())) + \
#             '''đ</td></tr>'''
#         html_content += '''</table>

#         <p style="margin:0;font-family:Arial, Helvetica, sans-serif;font-size:12px;color:#444;line-height:18px;font-weight:normal;">Trường hợp quý khách có những băn khoăn về đơn hàng, có thể liên hệ với chúng tôi theo số <b>(028) 38 351 056</b></p>'''

#         msg = EmailMultiAlternatives(
#             subject, message, EMAIL_HOST_USER, [recepient])
#         msg.attach_alternative(html_content, "text/html")
#         msg.send()

#         # clear the Giohang
#         giohang.clear()
#         result = "Đơn hàng đã được đặt thành công. Mời quý khách kiểm tra thông tin đơn hàng trong email!"
#         return render(request, 'khachhang/dathang.html',{'form': form,'fullname': kh.fullname,'email': kh.email,'phone': kh.phone, 'giohang': giohang, 'result': result })
#     # clear the Giohang
#     giohang.clear()
#     return render(request, 'khachhang/dathang.html',{'form': form,'fullname': kh.fullname,'email': kh.email,'phone': kh.phone, 'giohang': giohang, })
