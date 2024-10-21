from rest_framework import serializers

from .models import (
    Category,
    Product,
    ProductAttribute,
    AttributeGroup
)


class CategorySerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'slug',
            'parent',
            'description',
            'is_active',
            'children'
        ]

    @staticmethod
    def get_children(obj):

        children = obj.children.all()
        if children.exists():
            return CategorySerializer(children, many=True).data
        return None


class AttributeGroupSerializer(serializers.ModelSerializer):
    attributes = serializers.StringRelatedField(many=True)

    class Meta:
        model = AttributeGroup
        fields = [
            'id',
            'title',
            'attributes'
        ]


class ProductAttributeSerializer(serializers.ModelSerializer):
    attribute = serializers.StringRelatedField()

    class Meta:
        model = ProductAttribute
        fields = [
            'id',
            'attribute',
            'value',
        ]



class ProductSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    brand = serializers.StringRelatedField(allow_null=True)
    attribute_group = serializers.StringRelatedField(many=True)
    attributes = ProductAttributeSerializer(many=True)
    images = serializers.StringRelatedField(many=True)

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'description',
            'inventory',
            'status',
            'category',
            'brand',
            'attribute_group',
            'attributes',
            'images'

        ]
