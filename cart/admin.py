from django.contrib import admin
from .models import Cart


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ("user", "created_at", "updated_at")
    list_filter = ("user", "created_at", "updated_at")
    search_fields = ("user", "created_at", "updated_at")
