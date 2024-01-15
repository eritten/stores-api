from django.contrib import admin
from .models import Category, Product, Store, ProductImage

# Register your models here.


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']
    search_fields = ['name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'description']
    list_filter = ['title']
    search_fields = ['title', 'description']
    autocomplete_fields = ['stores']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['label']
    list_filter = ['label']
    search_fields = ['label']
    sortable_by = ['label']
