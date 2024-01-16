from .models import Store, Product, ProductImage, Category
from rest_framework import serializers


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['image']


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True)
    stores = serializers.StringRelatedField()

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price', 'images', 'stores']


class StoreSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Store
        fields = ['name', 'products']
