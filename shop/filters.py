import django_filters
from . import models


class ProductFilter(django_filters.FilterSet):
    """Filtering for the product list page"""
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains', label='Name')
    price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt', label='Price higher than:')
    price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt', label='Price lower than:')
    class Meta:
        model = models.Product
        fields = ['name', ]