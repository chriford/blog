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
