from django.urls import path
from . import views

urlpatterns = [
    path('shop/categories/', views.all_categories_view, name='all_categories'),
    path('shop/products/', views.all_products_view, name='all_products'),
    path('shop/category/<int:category_id>/', views.category_products_view, name='category_products'),
]
