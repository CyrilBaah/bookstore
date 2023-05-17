from django.urls import path

from . import views

urlpatterns = [
    path("register/", views.RegistrationAPIView.as_view(), name="create_user"),
    path("login/", views.LoginAPIView.as_view(), name="login_user"),
]
