from django.contrib import admin

from .models import Cart


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ["user", "book_name", "quantity"]
    list_filter = ["user", "quantity"]
    search_fields = ["user", "book_name", "quantity"]

    def book_name(self, obj):
        return obj.book.title
