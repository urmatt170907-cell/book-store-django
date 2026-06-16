from django.urls import path
from . import views

urlpatterns = [
    path(
        'create_basket/',
        views.BasketCreateView.as_view(),
        name='create_basket'
    ),

    path(
        'basket_list/',
        views.BasketListView.as_view(),
        name='basket_list'
    ),

    path(
        'basket_list/<int:id>/update/',
        views.BasketUpdateView.as_view(),
        name='update_basket'
    ),

    path(
        'basket_list/<int:id>/delete/',
        views.BasketDeleteView.as_view(),
        name='delete_basket'
    ),
]