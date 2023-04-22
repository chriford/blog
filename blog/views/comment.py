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
    if request.method == "POST":
        post = Post.objects.get(pk=pk)
        blog_comment = request.POST.get("comment", None)
        Comment.objects.create(post=post, comment=blog_comment)
        messages.success(request, "comment added")
        return redirect(
            reverse(
                "blog:post-view",
                kwargs={
                    "pk": post.pk,
                    "title": post.title,
                },
            )
        )
    else:
        return redirect("blog:posts")


@login_required(login_url=settings.LOGIN_REDIRECT_URL)
def comment_action(request, pk: int, action_type: str):
    comment = Comment.objects.get(pk=pk)
    if action_type == "delete":
        comment.delete()
        messages.success(request, "comment has been deleted successfully")
        return redirect(
            reverse(
                "blog:post-view",
                kwargs={
                    "pk": comment.post.pk,
                    "title": comment.post.title,
                },
            )
        )

    elif action_type == "update":
        if request.method == "POST":
            comment.comment = request.POST.get("comment")
            comment.save()
            return redirect(
            reverse(
                "blog:post-view",
                kwargs={
                    "pk": comment.post.pk,
                    "title": comment.post.title,
                },
            )
        )

    elif action_type == "like":
        blog_comment = request.POST.get("comment", None)
        Comment.objects.create(post=comment.post, comment=blog_comment)
        messages.success(request, "comment added")
        return redirect(
            reverse(
                "blog:post-view",
                kwargs={
                    "pk": comment.post.pk,
                    "title": comment.post.title,
                },
            )
        )

    else:
        return redirect(
            reverse(
                "blog:post-view",
                kwargs={
                    "pk": comment.post.pk,
                    "title": comment.post.title,
                },
            )
        )