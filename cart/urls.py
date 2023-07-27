from django.urls import path

from .views import CartCreateView, CartDetailView, CartListView

urlpatterns = [
    path("", CartListView.as_view(), name="list_cart"),
    path("create-cart/", CartCreateView.as_view(), name="create_cart"),
    path("my-cart/", CartDetailView.as_view(), name="my_cart"),
]
