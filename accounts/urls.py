from django.urls import path, include

from . import views

urlpatterns = [
    path("register/", views.RegistrationAPIView.as_view(), name="create_user"),
]