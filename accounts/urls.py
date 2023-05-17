from django.urls import include, path

from . import views

urlpatterns = [
    path("register/", views.RegistrationAPIView.as_view(), name="create_user"),
]
