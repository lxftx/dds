import django_filters

from cash.models import CashFlowRecord


class CashFlowRecordFilter(django_filters.FilterSet):
    date_from = django_filters.DateFilter(field_name="date", lookup_expr='gte')
    date_to = django_filters.DateFilter(field_name="date", lookup_expr='lte')
    status = django_filters.CharFilter(field_name="status__name", lookup_expr='icontains')
    type = django_filters.CharFilter(field_name="type__name", lookup_expr='icontains')
    category = django_filters.CharFilter(field_name="category__name", lookup_expr='icontains')
    subcategory = django_filters.CharFilter(field_name="subcategory__name", lookup_expr='icontains')

    class Meta:
        model = CashFlowRecord
        fields = ['date_to', 'date_from', 'status', 'type', 'category', 'subcategory']