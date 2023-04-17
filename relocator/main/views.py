from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from .models import *
from .forms import *
#def home(request):
#    return HttpResponse("Главная страница общая") 

def begin(request):
    return render(request, 'main/index.html') 

def autorisation(request):
    return render(request, 'main/autorization.html') 

def userApplication(request):
    return render(request, 'main/user/application.html') 

def userProfile(request):
    if request.method == 'POST':
        form = AddProfileForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.cleaned_data['user'] = get_object_or_404(User, id=form.cleaned_data['user'])
            print(form.cleaned_data)
            try:
                Personal_Info.objects.create(**form.cleaned_data)
                return redirect('begin')
            except Exception as e:
                form.add_error(None, f'Ошибка: {e}')

    else:
        form = AddProfileForm()

    return render(request, 'main/user/profile.html', {'form': form}) 

def userRelocatedEmployees(request):
    user = User.objects.all()
    return render(request, 'main/user/relocatedEmployees.html', {'user': user})  


def hr(request):
    return render(request, 'main/hr/base.html') 

def hrApplications(request):
    return render(request, 'main/hr/applications.html') 

def hrEmployeeProfile(request, appid):
    return render(request, 'main/hr/employeeProfile.html', {appid}) 
    #return HttpResponse(f"Заявка на релокацию номер {appid}") 



