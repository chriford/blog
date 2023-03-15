from django.urls import path, include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import (
    posts,
    management
)
app_name = 'blog'
urlpatterns = [
    path('', posts, name='index'),
    path('management/', management, name='management'),
    path('', posts, name='posts'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]