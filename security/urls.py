from django.conf import settings
from django.urls import path, include
from .views import (
    signin,
    signup,
    signout,
    profile,
    password_reset,
)
from django.contrib.auth import views as auth_views #import this

app_name = 'security'
urlpatterns = [
    path('login/', signin, name='login'),
    path('logout/', signout, name='logout'),
    path('user-profile/', profile, name='profile'),
    path('signup/', signup, name='signup'),
    
    path('forgot-password/', password_reset, name='forgot-password'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='auth/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="auth/password/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='auth/password_reset_complete.html'), name='password_reset_complete'),
]