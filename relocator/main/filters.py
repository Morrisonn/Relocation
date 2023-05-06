import django_filters
from .models import *


class RelocatedEmployeesFilter(django_filters.FilterSet):
    country = django_filters.CharFilter(lookup_expr='icontains', label='Страна', field_name='location__country')
    city = django_filters.CharFilter(lookup_expr='icontains', label='Город', field_name='location__city')

    class Meta: 
        model = Application
        fields = []
