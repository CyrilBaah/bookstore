from django.urls import path

from .views import BookCreateAPIView, BookListAPIView

urlpatterns = [
    path("create/", BookCreateAPIView.as_view(), name="create_book"),
    path("", BookListAPIView.as_view(), name="list_book"),
]
