from django.contrib import admin

from .models import (
    User,
    Profile,
)

@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    list_display = [
        'email',
        'username',
        'is_active',
        'is_staff',
        'is_superuser'
    ]
    search_fields = [
        'email',
        'username',
    ]


@admin.register(Profile)
class ProfileModelAdmin(admin.ModelAdmin):
    list_display = [
        'email',
        'first_name',
        'last_name',
        'phone_number',
        'phone_number2',
        'address',
        'created_at',
        'updated_at',
    ]
    search_fields = [
        'email',
        'first_name',
        'last_name',
    ]
