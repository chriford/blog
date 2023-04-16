import os

from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.shortcuts import (
    render,
    HttpResponse,
    redirect,
)
from blog.models import (
    Post,
    Category,
    Trash,
    Favorite,
    Comment,
)
from blog.forms import (
    PostForm,
    CategoryForm,
    ImageForm,
)
from security.models import (
    User,
)

from rolepermissions.roles import RolesManager
from rolepermissions.roles import get_user_roles
from rolepermissions.decorators import (
    has_role,
    has_role_decorator, 
    has_permission_decorator,
)

@login_required(login_url=settings.LOGIN_REDIRECT_URL)
@has_role_decorator("admin")
# @has_permission_decorator("can_manage_blog")
def management(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    users = User.objects.all()
    comments = Comment.objects.all()
    assigned_roles = get_user_roles(request.user)
    raw_assigned_roles = [role.get_name() for role in assigned_roles]
    available_roles = RolesManager.get_roles_names()
    context = {
        "post_count": posts.count(),
        "posts": posts,
        "category_count": categories.count(),
        "categories": categories,
        "comment_count": comments.count(),
        "user_count": users.count(),
        "users": users,
        "assigned_roles": raw_assigned_roles,
        "available_roles": list(available_roles),
    }
    return render(request, "blog/management.html", context)
