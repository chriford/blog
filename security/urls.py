from django.conf import settings
from django.urls import path, include
from .views import (
    signin,
    signup,
    password_reset,
)

app_name = 'security'
urlpatterns = [
    path('login/', signin, name='login'),
    path('signup/', signup, name='signup'),
    path('forgot-password/', password_reset, name='forgot-password'),
]