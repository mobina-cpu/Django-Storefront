from django.urls import path
from . import views


urlpatterns = [
    path('categories/', views.CategoryList.as_view()),
    path('categories/<int:category_id>/', views.ProductsByCategory.as_view()),
]