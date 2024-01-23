import django_filters
from provider.models import Provider


class ProviderFilter(django_filters.FilterSet):
    city = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Provider
        fields = ['country']
