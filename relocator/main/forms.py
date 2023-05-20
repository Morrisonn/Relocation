from django import forms
from .models import *


class AddProfileForm(forms.Form):
    first_name = forms.CharField(max_length=50, label="Имя")
    last_name = forms.CharField(max_length=50, label="Фамилия")
    middle_name = forms.CharField(max_length=50, label="Отчество")
    photo = forms.ImageField(required=False, label="Фото")
    gender = forms.ChoiceField(
        choices=[("male", "Мужской"), ("female", "Женский")],
        required=False,
        label="Пол",
    )
    rate = forms.DecimalField(
        max_digits=10, decimal_places=2, required=False, label="Ставка"
    )
    date_of_birth = forms.DateField(
        required=False,
        label="Дата рождения",
        widget=forms.DateInput(attrs={"type": "date"}),
    )
    work_experience = forms.IntegerField(min_value=0, label="Стаж (месяцев)")
    position = forms.CharField(max_length=50, label="Должность")
    email = forms.EmailField(label="email")
    phone_number = forms.CharField(max_length=20, label="Номер телефона")

class AddProfileForm(forms.Form):
    first_name = forms.CharField(max_length=50, label="Пометки")
    
# class CreateApplication(forms.Form):
