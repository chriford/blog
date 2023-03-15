from django.urls import path, include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import (
    posts,
    management,
    post_create,
    post_delete,
    post_update,
)

app_name = 'blog'
urlpatterns = [
    path('', posts, name='index'),
    path('management/', management, name='management'),
    path('post/view/', posts, name='posts'),
    path('post/create/', post_create, name='post-create'),
    path('post/<str:title>/delete/blog/<int:pk>/', post_delete, name='post-delete'),
    path('post/<str:title>/update/blog/<int:pk>/', post_update, name='post-update'),
    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]