from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),

    path(
        "books/",
        views.BookListView.as_view(),
        name="book_list"
    ),

    path(
        "books/create/",
        views.BookCreateView.as_view(),
        name="book_create"
    ),

    path(
        "books/<int:pk>/",
        views.BookDetailView.as_view(),
        name="book_detail"
    ),

    path(
        "search/",
        views.SearchBookView.as_view(),
        name="search_book"
    ),
]