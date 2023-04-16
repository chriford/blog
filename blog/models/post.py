import uuid
import logging
from datetime import timedelta

from django.db import models
from django.utils.translation import gettext_lazy as _

from blog.models.category import Category
from blog.models.timestamp import Timestamp


class Post(Timestamp):
    owner = models.ForeignKey(
        "security.User",
        related_name="user",
        help_text=_("The owner of this post."),
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )
    title = models.CharField(
        max_length=200,
        verbose_name=_("Title"),
        help_text=_("Title of the post"),
        null=True,
        blank=False,
    )
    category = models.ForeignKey(
        "blog.Category",
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        help_text=_("Select the category of this post"),
    )
    body = models.TextField(
        verbose_name=_("Body"),
        null=True,
    )
    is_active = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    delete_on = models.DateTimeField(
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ["-pk"]

    def __str__(self):
        return self.title

    def comment_objects(self):
        from blog.models import Comment

        post_comments = Comment.objects.filter(
            post=self,
        )
        return post_comments

    def voke_objects(self):
        from blog.models import Comment

        post_comments = Comment.objects.filter(
            post=self,
        )
        return post_comments

    @property
    def comments(self):
        return self.comment_objects()

    @property
    def total_comments(self):
        return self.comment_objects().count()

    @property
    def image_form(self):
        from blog.forms import ImageForm
        form = ImageForm(initial={'post': self})
        return form