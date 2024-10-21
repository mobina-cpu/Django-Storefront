from django.urls import path
from . import views

urlpatterns = [
    #category endpoints
    path('categories/', views.CategoryListView.as_view(), name='category-list'),
    path('categories/<int:category_id>/products/', views.CategoryProductsListView.as_view()),

    #brand endpoints
    path('brands/', views.BrandListView.as_view()),
    path('brands/<int:brand_id>/products/', views.BrandProductsListView.as_view()),

]