from django.contrib import admin
from .models import Author, Tag, Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Author)
admin.site.register(Tag)
