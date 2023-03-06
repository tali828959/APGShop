from django import forms
from . import models
from django.core.validators import RegexValidator


phone_validator = RegexValidator(
    r"((\([0-9]{3}\)[0-9]{9,15})|([0-9]{10,15}))", "Your phone number must be (xxx)xxxxxxxxx or 0xxxxxxxxx!")

class FormLienhe(forms.ModelForm):
    hoten = forms.CharField(max_length=150, label='Hoten', widget=forms.TextInput(attrs={
                           'placeholder': 'Enter your name', 'class': 'form-control fh5co_contact_text_box'}))
    sdt = forms.CharField(max_length=20, label='Phone', validators=[phone_validator], widget=forms.TextInput(
        attrs={'placeholder': 'Phone number',
               'class': 'form-control fh5co_contact_text_box',
               'pattern': '((\([0-9]{3}\)[0-9]{9,15})|([0-9]{10,15}))',
               'title': 'Your phone number must be (xxx)xxxxxxxxx or 0xxxxxxxxx'}))
    email = forms.EmailField(label='Email', widget=forms.TextInput(
        attrs={'placeholder': 'Email', 'class': 'form-control fh5co_contact_text_box'}))
    chude = forms.CharField(label='Subject', widget=forms.TextInput(
        attrs={'placeholder': 'Subject', 'class': 'form-control fh5co_contact_text_box'}))
    noidung = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': 'Message', 'class': 'form-control fh5co_contacts_message'}))

    class Meta:
        model = models.Lienhe
        fields = '__all__'


class FormKHACHHANG(forms.ModelForm):
    ten_kh = forms.CharField(max_length=500, widget=forms.TextInput())
    email = forms.EmailField(widget=forms.TextInput())
    mat_khau = forms.CharField(max_length=150, widget=forms.PasswordInput())
    xacnhan_matkhau = forms.CharField(max_length=150, label='confirm', widget=forms.PasswordInput())
    gioi_tinh = forms.ChoiceField(widget=forms.ChoiceField())
    dien_thoai = forms.CharField(max_length=20, widget=forms.TextInput(attrs={
                            'pattern': '((\([0-9]{3}\)[0-9]{9,15})|([0-9]{10,15}))', 'title': 'Your phone number must be (xxx)xxxxxxxxx or 0xxxxxxxxx'}))
    ngay_sinh = forms.DateField(widget=forms.DateField())
    dia_chi = forms.CharField(max_length=500, widget=forms.TextInput())

    class Meta:
        model = models.KHACHHANG
        fields = '__all__'


class KHACHHANGForm(forms.ModelForm):
    password = forms.CharField(
        max_length=150, label='Password', widget=forms.PasswordInput())
    confirm = forms.CharField(
        max_length=150, label='Confirm', widget=forms.PasswordInput())

    class Meta():
        model = models.KHACHHANG
        fields = ('fullname', 'email', 'password')

# class KHACHHANGProfileInfoForm(forms.ModelForm):
#     dia_chi = forms.CharField(max_length=500, widget=forms.TextInput())
#     dien_thoai = forms.CharField(max_length=20, label='Phone', widget=forms.TextInput(
#         attrs={'pattern': '((\([0-9]{3}\)[0-9]{9,15})|([0-9]{10,15}))',
#                'title': 'Your phone number must be (xxx)xxxxxxxxx or 0xxxxxxxxx'}))
#     image = forms.ImageField(required=False)

#     class Meta():
#         model = models.UserProfileInfo
#         exclude = ('user', )

# class Tim_Kiem(forms.ModelForm):
#     ten_sp = forms.CharField()
#     class Meta:
#         model = models.SANPHAM
#         fields = ('ten_sp',)