from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "rating", "slug"]
    list_filter = ["title", "author"]

    prepopulated_fields = {"slug": ("title",)}

