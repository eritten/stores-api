from django.shortcuts import render
from .serializers import ProductImageSerializer, ProductSerializer, StoreSerializer
from .models import ProductImage, Product, Store
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet


class StoreAPIView(ListModelMixin, GenericViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer


class ProductAPIView(ListModelMixin, GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
