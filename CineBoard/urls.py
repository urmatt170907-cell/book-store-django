from django.urls import path
from .views import (
    MovieListView, MovieDetailView,
    MovieCreateView, MovieUpdateView,
    MovieDeleteView, add_comment
)

urlpatterns = [
    path('', MovieListView.as_view(), name='movie_list'),
    path('movie/<int:pk>/', MovieDetailView.as_view(), name='movie_detail'),
    path('movie/create/', MovieCreateView.as_view(), name='movie_create'),
    path('movie/<int:pk>/update/', MovieUpdateView.as_view(), name='movie_update'),
    path('movie/<int:pk>/delete/', MovieDeleteView.as_view(), name='movie_delete'),
    path('movie/<int:pk>/comment/', add_comment, name='add_comment'),
]