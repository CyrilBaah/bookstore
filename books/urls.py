from django.urls import path

from .views import BookCreateAPIView, BookDeleteView, BookListAPIView, BookUpdateAPIView

urlpatterns = [
    path("create/", BookCreateAPIView.as_view(), name="create_book"),
    path("", BookListAPIView.as_view(), name="list_book"),
    path("update/<int:pk>/", BookUpdateAPIView.as_view(), name="update_book"),
    path("delete/<int:pk>/", BookDeleteView.as_view(), name="delete_book"),
]
