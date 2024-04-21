from django.shortcuts import render
from .serializers import *
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from django.db.models import Prefetch

# Create your views here.


class Pagination(PageNumberPagination):

    page_size = 1
    page_query_param = 'page_size'
    max_page_size = 1000


class FoodCategoryList(generics.ListAPIView):

    """Все категории"""

    serializer_class = FoodCategorySerializer
    pagination_class = Pagination

    def get_queryset(self):
        queryset = FoodCategory.objects.all()
        subcategory_name = self.request.query_params.get('is_publish', True)
        if subcategory_name is not None:
            prefetch_filtered_products = Prefetch(
                'food',
                Food.objects.filter(is_publish=subcategory_name)
            )
            return queryset.prefetch_related(prefetch_filtered_products)
        return queryset.prefetch_related('food')










