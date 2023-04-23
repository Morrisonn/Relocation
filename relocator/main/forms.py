from django import forms 
from .models import *

class AddProfileForm(forms.Form):
    first_name = forms.CharField(max_length=50, label = "Имя")
    last_name = forms.CharField(max_length=50, label = "Фамилия")
    middle_name = forms.CharField(max_length=50 , label = "Отчество")
    work_experience = forms.IntegerField(min_value=0 , label = "Стаж работы")
    position = forms.CharField(max_length=50 , label = "Должность")
    email = forms.EmailField(label = "email")
    phone_number = forms.CharField(max_length=20, label = "Номер телефона")
    