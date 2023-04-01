import os

from django.urls import reverse
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.urls import reverse_lazy
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

@login_required(login_url=settings.LOGIN_REDIRECT_URL)
def comment(request, pk, title, *args, **kwargs):
    if request.method == 'POST':
        post = Post.objects.get(pk=pk)
        blog_comment = request.POST.get('comment', None)
        Comment.objects.create(post=post, comment=blog_comment)
        messages.success(request, 'comment added')
        return redirect(reverse('blog:comment', kwargs={
            'pk': post.pk,
            'title': post.title,
        }))
    else:
        return redirect('blog:posts')