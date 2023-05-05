from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import logout

from relocator import settings
from .models import *
from .forms import *
#def home(request):
#    return HttpResponse("Главная страница общая") 

def logout_view(request):
    logout(request)
    return redirect('login')

def user(request):
    return render(request, 'main/user/base.html') 

def begin(request):
    if not request.user.is_authenticated:
        return redirect("login")
    else:
        print(request.user.role)
        print(request.user.is_superuser)
        if request.user.role == "0":
            return redirect("user")
        elif request.user.role == "1":
            return redirect("hr")
        elif request.user.is_superuser == True:
            return redirect("/admin/")
        else:
            return redirect("/autorization/login/")
    return render(request, 'main/index.html') 

def autorisation(request):
    return render(request, 'main/autorization.html') 

def userApplication(request):
    return render(request, 'main/user/application.html') 

def userProfile(request):
    personal_info = Personal_Info.objects.filter(user_id = request.user.id)
    personal_info_len = len(Personal_Info.objects.filter(user_id = request.user.id))
    if not request.user.is_authenticated:
        return HttpResponse("403", status=403)
    else:
        user = User.objects.get(id=request.user.id)
        
    if request.method == 'POST':
        form = AddProfileForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            # form.cleaned_data['user'] = get_object_or_404(User, id=form.cleaned_data['user'])
            form.cleaned_data['user'] = user
            print(form.cleaned_data)
            try:
                Personal_Info.objects.create(**form.cleaned_data)
                return redirect('begin')
            except Exception as e:
                form.add_error(None, f'Ошибка: {e}')

    else:
        form = AddProfileForm()
    return render(request, 'main/user/profile.html', {'form': form, 'personal_info': personal_info, 'personal_info_len': personal_info_len}) 

def userRelocatedEmployees(request):
    applications = Application.objects.filter(status='done').select_related("user", "location")
    for item in applications:
        item.personal_info = Personal_Info.objects.get(user=item.user)

    context = {
        'YANDEX_MAPS_API_KEY': settings.YANDEX_MAPS_API_KEY,
    }
    return render(
        request,
        'main/user/relocatedEmployees.html',
        {
            'applications': applications,
        }
    )  

def userNews(request):
    return render(request, 'main/user/news.html') 


def hr(request):
    return render(request, 'main/hr/base.html') 

def hrApplications(request):
    return render(request, 'main/hr/applications.html') 

def hrEmployeeProfile(request, appid):
    return render(request, 'main/hr/employeeProfile.html', {appid}) 
    #return HttpResponse(f"Заявка на релокацию номер {appid}") 



