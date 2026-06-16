from django.urls import path
from . import views

urlpatterns = [
    path(
        "register/",
        views.CandidateCreateView.as_view(),
        name="register"
    ),

    path(
        "login/",
        views.LoginView.as_view(),
        name="login"
    ),

    path(
        "candidates/",
        views.CandidateListView.as_view(),
        name="candidate_list"
    ),
]