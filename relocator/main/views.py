from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import logout
from .filters import *
from relocator import settings
from .models import *
from .forms import *
from django.db.models import Q


def logout_view(request):
    logout(request)
    return redirect("login")


def user(request):
    new_username = Personal_Info.objects.filter(user_id=request.user.id)
    new_username_len = len(new_username)
    return render(
        request,
        "main/user/base.html",
        {
            "new_username": new_username.first(),
            "new_username_len": new_username_len,
        },
    )


def begin(request):
    if not request.user.is_authenticated:
        return redirect("login")
    else:
        # print(request.user.role)
        # print(request.user.is_superuser)
        if request.user.role == "0":
            return redirect("user")
        elif request.user.role == "1":
            return redirect("hr")
        elif request.user.is_superuser == True:
            return redirect("/admin/")
        else:
            return redirect("/autorization/login/")
    return render(request, "main/index.html")


def autorisation(request):
    return render(request, "main/autorization.html")

def userAccount(request):
    new_username = Personal_Info.objects.filter(user_id=request.user.id)
    new_username_len = len(new_username)
    news_content = News.objects.all()
    return render(
        request,
        "main/user/account.html",
        {
            "new_username": new_username.first(),
            "new_username_len": new_username_len,
            "news_content" : news_content,
        },
    )

def userApplication(request):
    user_application = Application.objects.filter(user_id=request.user.id)
    user_application_len = len(user_application)
    if user_application_len == 0:
        status = None
    else:
        status = user_application.first().status

    new_username = Personal_Info.objects.filter(user_id=request.user.id)
    new_username_len = len(new_username)
    locations = Location.objects.all()

    print("==>", user_application)
    print("==>", user_application_len)
    print("==>", locations)


    # print(f"smh {request} {request.POST}")
    # selected_location_id = int(request.POST.get('selected_location'))
    # print('---->', selected_location_id, type(selected_location_id))
    # selected_location = Location.objects.get(id=selected_location_id)

    context = {
        "YANDEX_MAPS_API_KEY": settings.YANDEX_MAPS_API_KEY,
    }
    return render(
        request,
        "main/user/application.html",
        {
            "new_username": new_username.first(),
            "new_username_len": new_username_len,
            "user_application": user_application.first(),
            "user_application_len": user_application_len,
            "locations": locations,
            "status": status,
        },
    )


def newUserApplication(request):
    # print(f"smh new {request} {request.POST}")
    Application(
        user_id=request.user.id,
        location_id=int(request.POST.get("selected_location")),
        status="first",
    ).save()
    return redirect("userApplication")


def userProfile(request):
    new_username = Personal_Info.objects.filter(user_id=request.user.id)
    new_username_len = len(new_username)
    personal_info = Personal_Info.objects.filter(user_id=request.user.id)
    personal_info_len = len(Personal_Info.objects.filter(user_id=request.user.id))
    if not request.user.is_authenticated:
        return HttpResponse("403", status=403)
    else:
        user = User.objects.get(id=request.user.id)
    if request.method == "POST":
        form = AddProfileForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            # form.cleaned_data['user'] = get_object_or_404(User, id=form.cleaned_data['user'])
            form.cleaned_data["user"] = user
            # print(form.cleaned_data)
            try:
                Personal_Info.objects.create(**form.cleaned_data)
                return redirect("begin")
            except Exception as e:
                form.add_error(None, f"Ошибка: {e}")
    else:
        form = AddProfileForm()
    return render(
        request,
        "main/user/profile.html",
        {
            "form": form,
            "personal_info": personal_info,
            "personal_info_len": personal_info_len,
            "new_username": new_username.first(),
            "new_username_len": new_username_len,
        },
    )


def userRelocatedEmployees(request):
    new_username = Personal_Info.objects.filter(user_id=request.user.id)
    new_username_len = len(new_username)

    applications = Application.objects.filter(status="first").select_related(
        "user", "location"
    )
    locations_filter = RelocatedEmployeesFilter(request.GET, queryset=applications)
    applications = locations_filter.qs
    print("==>>", applications)
    for item in applications:
        print("==>>", item.user)
        try:
            item.personal_info = Personal_Info.objects.get(user=item.user)
        except:
            print("Ексепт")

    context = {
        "YANDEX_MAPS_API_KEY": settings.YANDEX_MAPS_API_KEY,
    }
    return render(
        request,
        "main/user/relocatedEmployees.html",
        {
            "applications": applications,
            "locations_filter": locations_filter,
            "new_username": new_username.first(),
            "new_username_len": new_username_len,
        },
    )


def userNews(request):
    new_username = Personal_Info.objects.filter(user_id=request.user.id)
    new_username_len = len(new_username)
    news_content = News.objects.all()
    return render(
        request,
        "main/user/news.html",
        {
            "new_username": new_username.first(),
            "new_username_len": new_username_len,
            "news_content" : news_content,
        },
    )


def hr(request):
    return render(request, "main/hr/base.html")


def hrApplications(request):
    # applications = Personal_Info.objects.filter(Q(user__application__isnull=False))
    # applications = Application.objects.select_related("user", "location")
    infos = Personal_Info.objects.select_related("user")
    infos_filter = PersonalInfoFilter(request.GET, queryset=infos)
    infos = infos_filter.qs

    applications = Application.objects.none()
    for info in infos:
        applications = applications.union(Application.objects.filter(user_id=info.user.id))
    for item in applications:
        item.personal_info = Personal_Info.objects.get(user=item.user)

    print("->>>>", applications)
    return render(
        request,
        "main/hr/applications.html",
        {
            "applications": applications,
            "infos_filter": infos_filter,
        },
    )


def hr_userPage(request, userId):
    personal_info = Personal_Info.objects.filter(user_id=userId)
    user_application = Application.objects.filter(user_id=userId)
    user_application_len = len(user_application)
    if user_application_len == 0:
        status = None
    else:
        status = user_application.first().status
    # personal_info_len = len(Personal_Info.objects.filter(user_id=userId))
    return render(
        request, 
        "main/hr/userPage.html", 
        {
            "userId": userId,
            "personal_info": personal_info,
            "user_application": user_application.first(),
            "status" : status,
        }
    )
    # return HttpResponse(f"Заявка на релокацию номер {appid}")
