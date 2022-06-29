from django.db.models import Q
from django_filters import rest_framework as filters
from rest_framework.viewsets import ModelViewSet

from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    search_fields = ['title', 'description']

'''
1 вариант. так только по одному полю можно добавить для фильтрации.
Для поиска по описанию или по идентификатору, нужно 
создавать новые атрибуты класса.
'''
# class ProductFilter(filters.FilterSet):
#     products = filters.CharFilter(
#         field_name='products__title',
#         # field_name='products__title,products__description',
#         lookup_expr='icontains',
#     )
#
#     class Meta:
#         model = Stock
#         fields = ['products']


class ProductFilter(filters.FilterSet):
    products = filters.CharFilter(method='search_filter')

    def search_filter(self, queryset, name, value):
        return queryset.filter(Q(products__title__icontains=value) |
                               Q(products__description__icontains=value)
                               ).distinct()


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    filterset_class = ProductFilter
