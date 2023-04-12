from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Главная страница общая") 

def user(request):
    return HttpResponse("Главная страница сотрудника") 

def userProfile(request):
    return HttpResponse("Профиль сотрудника") 

def userRelocatedEmployees(request):
    return HttpResponse("Релоцированные струдники") 


def hr(request):
    return HttpResponse("Главная страница hr") 

def hrApplication(request, appid):
    return HttpResponse(f"Заявка на релокацию номер {appid}") 


