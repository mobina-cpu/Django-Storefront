from django.contrib import admin

from .models import (
    Category,
    Brand,
    Attribute,
    AttributeGroup,
    Product,
    ProductAttribute,
    ProductImage
)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'slug',
        'parent',
        'is_active'
    ]
    search_fields = [
        'name',
        'slug'
    ]
    list_filter = ['is_active']
    prepopulated_fields = {'slug': ['name']}
    ordering = ['name']


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'slug'
    ]
    search_fields = [
        'name',
        'slug'
    ]
    prepopulated_fields = {'slug':['name']}
    ordering = ['name']


@admin.register(Attribute)
class AttributeAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'code_name'
    ]
    search_fields = [
        'title',
        'code_name'
    ]
    ordering = ['title']


@admin.register(AttributeGroup)
class AttributeGroupAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']
    filter_horizontal = ['attributes']


class ProductAttributeInline(admin.TabularInline):
    model = ProductAttribute
    extra = 1


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'category',
        'brand',
        'status',
        'inventory'
    ]
    search_fields = [
        'name',
        'category__name',
        'brand__name'
    ]
    list_filter = [
        'status',
        'category',
        'brand'
    ]
    inlines = [ProductAttributeInline, ProductImageInline]
    ordering = ['name']


@admin.register(ProductAttribute)
class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = [
        'product',
        'attribute',
        'value'
    ]
    search_fields = [
        'product__name',
        'attribute__title'
    ]
    ordering = ['product']


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = [
        'product',
        'is_primary',
        'image'
    ]
    search_fields = ['product__name']
    list_filter = ['is_primary']
    ordering = ['product']
