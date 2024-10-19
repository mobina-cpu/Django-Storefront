from rest_framework import serializers

from product.models import Category


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

    def get_children(self, obj):

        children = obj.children.all()
        if children.exists():
            return CategorySerializer(children, many=True).data
        return None