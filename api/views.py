from django.shortcuts import render
from .serializers import ProductImageSerializer, ProductSerializer, StoreSerializer
from .models import ProductImage, Product, Store
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet


class StoreAPIView(ListModelMixin, GenericViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer


class ProductAPIView(ListModelMixin, GenericViewSet):
    queryset = Product.objects.prefetch_related(
        'stores').prefetch_related('images').all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        product_name = self.request.query_params.get("product_name")
        return Product.objects.prefetch_related('stores').prefetch_related('images').filter(title=product_name)
