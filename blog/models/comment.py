import uuid
import logging

from django.db import models
from django.utils.translation import gettext_lazy as _

from blog.models.category import Category
from blog.models.timestamp import Timestamp

class Comment(Timestamp):
    post = models.ForeignKey(
        verbose_name=_("Post"),
        to='blog.Post',
        on_delete=models.CASCADE,
        null=True,
        blank=False,
    )
    comment = models.CharField(
        verbose_name=_("Comment"),
        max_length=300,
        null=True,
        blank=False,
    )
    
    def __str__(self):
        return f"{self.post.title} - comment-{self.pk}"