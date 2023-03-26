import uuid
import logging
from datetime import timedelta

from django.db import models
from django.utils.translation import gettext_lazy as _

from blog.models.category import Category
from blog.models.timestamp import Timestamp


class Voke(Timestamp):
    user = models.OneToOneField(
        'security.User',
        help_text=_("The owner of this like."),
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )
    upvoke = models.PositiveIntegerField(
        verbose_name=_("Upvoke"),
        help_text=_("Upvoke or like count"),
        null=True,
        blank=True,
        default=0,
    )
    downvoke = models.PositiveIntegerField(
        verbose_name=_("Downvoke"),
        help_text=_("Downvoke or diskike count"),
        null=True,
        blank=True,
        default=0,
    )
    is_liked = models.BooleanField(default=False)
    is_disliked = models.BooleanField(default=False)
    is_neutral = models.BooleanField(default=True)
    
    def __str__(self):
        return self.is_neutral


