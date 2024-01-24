from django.shortcuts import render
from .serializers import ProductImageSerializer, ProductSerializer, StoreSerializer
from .models import ProductImage, Product, Store
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet
from django.db.models import Q
from rest_framework import filters


class StoreAPIView(ListModelMixin, GenericViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer


class ProductAPIView(ListModelMixin, GenericViewSet):
    queryset = Product.objects.prefetch_related(
        'stores').prefetch_related('images').all()
    serializer_class = ProductSerializer
    search_fields = ['title', 'description']
    filter_backends = [filters.SearchFilter]
