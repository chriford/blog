import uuid
import logging
from datetime import timedelta

from django.db import models
from django.utils.translation import gettext_lazy as _

from blog.models.category import Category
from blog.models.timestamp import Timestamp


class Voke(Timestamp):
    post = models.OneToOneField(
        "blog.Post",
        help_text=_("The owner of this like."),
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )
    table = models.CharField(
        verbose_name=_("Table"),
        max_length=100,
        null=True,
        blank=False,
    )
    is_liked = models.BooleanField(default=False)
    is_disliked = models.BooleanField(default=False)
    is_neutral = models.BooleanField(default=True)

    def __str__(self):
        return self.is_neutral
