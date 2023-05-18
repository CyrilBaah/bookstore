from django.urls import include, path
from rest_framework_simplejwt.views import TokenRefreshView

from . import views

urlpatterns = [
    path("register/", views.RegistrationAPIView.as_view(), name="create_user"),
    path("login/", views.LoginAPIView.as_view(), name="login_user"),
    path(
        "change_password/", views.ChangePasswordView.as_view(), name="change_password"
    ),
    path(
        "password_reset/",
        include("django_rest_passwordreset.urls", namespace="password_reset"),
    ),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
