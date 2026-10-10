
from django.urls import path

from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path(
        "transactions/add/",
        views.transaction_create,
        name="transaction_create",
    ),
    path(
        "transactions/<int:pk>/",
        views.transaction_detail,
        name="transaction_detail",
    ),
    path(
        "transactions/<int:pk>/edit/",
        views.transaction_edit,
        name="transaction_edit",
    ),
    path(
        "transactions/<int:pk>/delete/",
        views.transaction_delete,
        name="transaction_delete",
    ),
    path("signup/", views.signup, name="signup"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
]
