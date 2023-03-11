from django.urls import path, include
from .views import (
    posts,
    management
)
app_name = 'blog'
urlpatterns = [
    path('', posts, name='index'),
    path('management/', management, name='management'),
    path('', posts, name='posts'),
]