from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Category, Product
from .serializers import (
    CategorySerializer,
    ProductSerializer
)


class CategoryList(APIView):
    @staticmethod
    def get(request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)

        return Response(serializer.data)


class ProductsByCategoryAPIView(APIView):
    serializer_class = ProductSerializer

    @staticmethod
    def get(request, category_id):
        try :
            category = Category.objects.get(id=category_id)

        except Category.DoesNotExist:
            return Response(
                {"detail": "Category does not exist"}, status=status.HTTP_404_NOT_FOUND
            )
        products = Product.objects.filter(category=category)
        serializer = ProductSerializer(products, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)



