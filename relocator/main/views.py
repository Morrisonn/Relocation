from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import logout
from .models import *
from .forms import *
#def home(request):
#    return HttpResponse("Главная страница общая") 

def logout_view(request):
    logout(request)
    return redirect('login')

def user(request):
    context = Personal_Info.objects.filter(user_id = request.user.id)
    context_len = int(len(Personal_Info.objects.filter(user_id = request.user.id)))
    print("=>", context_len)
    print("=>", context)
    return render(request, 'main/user/base.html', {'context': context, 'context_len':context_len}) 

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



