import uuid
import logging
from datetime import timedelta

from django.db import models
from django.utils.translation import gettext_lazy as _

from blog.models.category import Category
from blog.models.timestamp import Timestamp


class Voke(Timestamp):
    
    user = models.ForeignKey(
        "security.User",
        help_text=_("The owner of this like."),
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )
    entry_pk = models.PositiveIntegerField(
        null=True,
        help_text=_("The primary key of an entry eg comment or post, etc."),
        unique=True,
    )
    table = models.CharField(
        verbose_name=_("Table"),
        max_length=100,
        null=True,
        blank=False,
    )
    is_liked = models.BooleanField(default=False)
    is_disliked = models.BooleanField(default=False)
    
    def save(self, *args, **kwargs):
        if self.is_liked:
            self.is_disliked = False
        
        if self.is_disliked:
            self.is_liked = False
    
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.user.username
