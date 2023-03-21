import uuid
import logging
from datetime import timedelta

from django.db import models
from django.utils.translation import gettext_lazy as _

from blog.models.category import Category
from blog.models.timestamp import Timestamp


class Like(Timestamp):
    liker = models.ForeignKey(
        'security.User',
        related_name='liker',
        help_text=_("The owner of this like."),
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )
    like = models.PositiveIntegerField(
        verbose_name=_("Like"),
        null=True,
        blank=True,
        default=0,
    )
    dislike = models.PositiveIntegerField(
        verbose_name=_("Dislike"),
        null=True,
        blank=True,
        default=0,
    )
    is_liked = models.BooleanField(default=False)
    is_disliked = models.BooleanField(default=False)
    is_neutral = models.BooleanField(default=True)
    
    def __str__(self):
        return self.is_neutral


