from django_filters import DateFromToRangeFilter
from django_filters.widgets import RangeWidget

from .models import *
import django_filters


class QuestionFilter(django_filters.FilterSet):
    class Meta:
        model = question
        created_on = django_filters.DateFilter()
        fields = ['categorie', 'created_on']

