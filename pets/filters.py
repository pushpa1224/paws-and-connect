import django_filters
from .models import Pet


class PetFilter(django_filters.FilterSet):
    location = django_filters.CharFilter(lookup_expr='icontains')
    breed = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Pet
        fields = ['animal_type', 'gender', 'status', 'location', 'breed']
