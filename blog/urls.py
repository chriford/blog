from django.urls import path, include
from .views import (
    posts,
)
app_name = 'blog'
urlpatterns = [
    path('', posts, name='posts'),
]