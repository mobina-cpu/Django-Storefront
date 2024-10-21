from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework import (
    status,
    generics
)

from .models import (
    Category,
    Product,
    Brand
)
from .serializers import (
    CategorySerializer,
    ProductSerializer,
    BrandSerializer
)
from .pagination import DefaultPageNumberPagination


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.filter(parent=None)
    serializer_class = CategorySerializer
    pagination_class = DefaultPageNumberPagination

    @staticmethod
    def post(request):
        if request.user.is_staff:
            serializer = CategorySerializer(data=request.data)

            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            return Response(
                {"detail": "You do not have permission to perform this action."}, status=status.HTTP_403_FORBIDDEN
            )


class CategoryProductsListView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        try:
            category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            raise NotFound(detail="Category not found.")

        return Product.objects.filter(category=category)


class BrandListView(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    pagination_class = DefaultPageNumberPagination


class BrandProductsListView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        brand_id = self.kwargs['brand_id']
        try:
            brand = Brand.objects.get(id=brand_id)
        except Brand.DoesNotExist:
            raise NotFound(detail="Brand not found.")

        return Product.objects.filter(brand=brand)
