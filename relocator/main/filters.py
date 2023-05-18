import django_filters
from .models import *


class RelocatedEmployeesFilter(django_filters.FilterSet):
    country = django_filters.CharFilter(
        lookup_expr="icontains", label="Страна", field_name="location__country"
    )
    city = django_filters.CharFilter(
        lookup_expr="icontains", label="Город", field_name="location__city"
    )

    class Meta:
        model = Application
        fields = []


class PersonalInfoFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(
        lookup_expr="icontains", label="Имя", field_name="first_name"
    )
    last_name = django_filters.CharFilter(
        lookup_expr="icontains", label="Фамилия", field_name="last_name"
    )
    middle_name = django_filters.CharFilter(
        lookup_expr="icontains", label="Отчество", field_name="middle_name"
    )

    class Meta:
        model = Personal_Info
        fields = []
