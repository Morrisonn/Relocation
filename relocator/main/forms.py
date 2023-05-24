from django import forms
from .models import *


class AddProfileForm(forms.Form):
    first_name = forms.CharField(max_length=50, label="Имя")
    last_name = forms.CharField(max_length=50, label="Фамилия")
    middle_name = forms.CharField(max_length=50, label="Отчество")
    # photo = forms.ImageField(required=False, label="Фото")
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

class InterviewLinkForm(forms.ModelForm):
    class Meta:
        model = Interview
        fields = ['link', 'datetime']
        widgets = {
            'datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }
        labels = {'link': 'Ссылка на собеседование', 'datetime':'Дата и время собеседования:'}

class InterviewNotesForm(forms.ModelForm):
    notes = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Interview
        fields = ['notes']
        labels = {'notes': 'Заметки'}    

class CheckListForm(forms.ModelForm):
    status = forms.BooleanField(initial=False, widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Check_list
        fields = ['name', 'status']
        labels = {
            'name': '',
        }
        label_suffix = 'л'

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['review', 'rating']
        labels = {
            'review': '',
            'rating': '',
        }
# class CreateApplication(forms.Form):