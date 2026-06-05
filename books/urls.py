from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('books/', views.book_list_view, name='book_list'),
    path('books/create/', views.book_create_view, name='book_create'),
    path('books/<int:pk>/', views.book_detail_view, name='book_detail'),
]
