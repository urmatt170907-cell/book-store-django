from django.urls import path
from .views import *

urlpatterns = [
    path('', MovieListView.as_view(), name='movie_list'),
    path('movie/<int:pk>/', MovieDetailView.as_view(), name='movie_detail'),
    path('create/', MovieCreateView.as_view(), name='movie_create'),
    path('update/<int:pk>/', MovieUpdateView.as_view(), name='movie_update'),
    path('delete/<int:pk>/', MovieDeleteView.as_view(), name='movie_delete'),
    path('search/', MovieSearchView.as_view(), name='movie_search'),
    path('genre/<int:pk>/', GenreMovieView.as_view(), name='genre_movies'),
    path('comment/<int:pk>/', AddCommentView.as_view(), name='add_comment'),
    path('vip/<int:pk>/', BookVIPView.as_view(), name='book_vip'),
    path('register/', RegisterView.as_view(), name='register'),
]