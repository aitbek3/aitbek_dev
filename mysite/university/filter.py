from django_filters.rest_framework import FilterSet
from .models import Faculty


class MovieFilter(FilterSet):
    class Meta:
        model = Faculty
        fields = {
            'name'
        }