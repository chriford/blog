from django.conf import settings
from django.urls import path, include
from .views import (
    signin,
    signup,
    logout,
    profile,
    password_reset,
)

app_name = 'security'
urlpatterns = [
    path('login/', signin, name='login'),
    path('logout/', logout, name='logout'),
    path('user-profile/', profile, name='profile'),
    path('signup/', signup, name='signup'),
    path('forgot-password/', password_reset, name='forgot-password'),
]