import django_filters
from django_filters.filters import CharFilter
from search_app.models import Question
from django_filters import CharFilter

class QuestionFilter(django_filters.FilterSet):
    quest = CharFilter(field_name='questions', lookup_expr='icontains')
    tag = CharFilter(field_name='tags', lookup_expr='icontains')
    vote = CharFilter(field_name='vote_count', lookup_expr='exact')
    
