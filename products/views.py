from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils.translation import get_language
from products.models import Product, Category
from .serializers import ProductSerializer, CategorySerializer

class ProductViewSet(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['translations__title', 'translations__description']

class ProductDetailViewSet(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CategoryViewSet(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = LimitOffsetPagination
    search_fields = ['translations__title', 'translations__description']
    

class CategoryDetailViewSet(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

