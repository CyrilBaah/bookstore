from django.urls import path

from .views import BookCreateAPIView

urlpatterns = [
    path("create/", BookCreateAPIView.as_view(), name="create_book"),
]
