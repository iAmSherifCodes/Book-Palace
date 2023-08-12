from django_filters import FilterSet

from .models import Book


class CustomFilter(FilterSet):
    class Meta:
        model = Book
        fields = {
            'author_id': ["exact"],
            'author__first_name': ['exact'],
            'title': ['exact'],
            'copies': ['gt', 'lt']
        }
