from django.contrib import admin
from blog.models import (
    Category,
)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','created_at','updated_at']
    search_fields = ['name',]
    list_per_page = 20

