from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import logout
from .filters import *
from relocator import settings
from .models import *
from .forms import *
from django.db.models import Q
from django.core.mail import send_mail
from django.forms import formset_factory


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
    interview = Interview.objects.filter(application_id = user_application.first().id)
    link = interview.first().link
    datetime = interview.first().datetime

    # print("==>", user_application)
    # print("==>", user_application_len)
    # print("==>", locations)

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
            "link" : link,
            "datetime" : datetime,
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
    notes = Interview.objects.filter(application_id = user_application.first().id)
    if user_application_len == 0:
        status = None
    else:
        status = user_application.first().status
    # personal_info_len = len(Personal_Info.objects.filter(user_id=userId))
    form = None
    formset = None
    if request.method == 'POST':
        if user_application.first().status == "first":
            form = InterviewLinkForm(request.POST)
            if form.is_valid():
                link = form.cleaned_data['link']
                time = form.cleaned_data['datetime']
                datetime = timezone.localtime(time)  
                formatted_datetime = datetime.strftime('%Y-%m-%d %H:%M')
                message = f"""Здравствуйте {personal_info.first().first_name}!
HR готов провести собеседование.
Оно состоится {formatted_datetime}
Ссылка:
{link}"""
                send_mail('Собеседование', message, 'mixasa.mk@gmail.com', ['mixasa.mk@gmail.com'])
                form.cleaned_data["application_id"] = user_application.first().id
                print("8888888888", form.cleaned_data, user_application)
                Interview.objects.create(**form.cleaned_data)
                application = user_application.first()
                application.status = "second"
                application.save()
                return redirect(request.path)
        elif user_application.first().status == "second":
            form = InterviewNotesForm(request.POST)
            if form.is_valid():
                application = user_application.first()
                interview = Interview.objects.get(application=application)
                interview.notes = form.cleaned_data['notes']
                interview.save()
                application.status = "third"
                application.save()
                return redirect(request.path)
        elif user_application.first().status == "third":
                CheckListFormSet = formset_factory(CheckListForm, extra=1)
                formset = CheckListFormSet(request.POST, prefix='checklist')
                print("***********************", formset)
                if formset.is_valid():
                    for i, form in enumerate(formset):
                        if form.has_changed():
                            check_list = form.save(commit=False)
                            check_list.application = user_application.first()

                            # Проверяем наличие поля 'name' в cleaned_data
                            if 'name' in form.cleaned_data:
                                check_list.name = form.cleaned_data['name']
                            else:
                                check_list.name = 'лол'  # Установите значение по умолчанию или игнорируйте поле

                            check_list.status = False
                            check_list.save()
                    return redirect(request.path)
        elif user_application.first().status == "third":
            formset = CheckListFormSet(prefix='checklist', initial=[{'name': ''}])
    else:
        if user_application.first().status == "first":
            form = InterviewLinkForm()
        elif user_application.first().status == "second":
            form = InterviewNotesForm()
        elif user_application.first().status == "third":
            CheckListFormSet = formset_factory(CheckListForm, extra=1)
            formset = CheckListFormSet(prefix='checklist')
    iid = Application.objects.filter(user_id = userId) 
    return render(
        request, 
        "main/hr/userPage.html", 
        {
            "userId": userId,
            "personal_info": personal_info,
            "user_application": user_application.first(),
            "status" : status,
            "notes" : notes,
            "form": form,
            "formset": formset,
            # "formset": formset if user_application.first().status == "third" else None,
        }
    )
    # return HttpResponse(f"Заявка на релокацию номер {appid}")

def hr_userProfile(request, userId):
    personal_info = Personal_Info.objects.filter(user_id=userId)
    return render(
        request, 
        "main/hr/userProfile.html", 
        {
            "userId": userId,
            "personal_info": personal_info,
        }
    )
    # return HttpResponse(f"Заявка на релокацию номер {appid}")

def hrNews(request):
    new_username = Personal_Info.objects.filter(user_id=request.user.id)
    new_username_len = len(new_username)
    news_content = News.objects.all()
    return render(
        request,
        "main/hr/news.html",
        {
            "new_username": new_username.first(),
            "new_username_len": new_username_len,
            "news_content" : news_content,
        },
    )