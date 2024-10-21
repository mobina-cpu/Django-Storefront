from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework import (
    status,
    generics
)

from .models import (
    Category,
    Product
)
from .serializers import (
    CategorySerializer,
    ProductSerializer
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




