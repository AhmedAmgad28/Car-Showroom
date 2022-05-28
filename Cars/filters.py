import django_filters
from .models import UsedCar

class BrandFilter(django_filters.FilterSet):
    class Meta:
        model = UsedCar
        fields = ['brand']