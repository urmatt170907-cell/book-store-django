from django.urls import path
from . import views

urlpatterns = [
    path('tours/', views.horse_tour_view, name='horse_tours'),
    path('tours/create-category/', views.create_tour_category_view, name='create_tour_category'),
    path('tours/create-tour/', views.create_horse_tour_view, name='create_horse_tour'),
    path('tours/create-horse/', views.create_horse_view, name='create_horse'),
    path('tours/book/', views.book_horse_view, name='book_horse'),
    path('tours/comment/', views.add_comment_view, name='add_comment'),
]
