from django.contrib import admin
from blog.models import (
    Category,
    Post,
)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','created_at','updated_at']
    search_fields = ['name',]
    list_per_page = 20


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['owner','title', 'created_at','updated_at']
    search_fields = ['title','owner']
    list_filter = ['owner', 'category']
    list_per_page = 25

