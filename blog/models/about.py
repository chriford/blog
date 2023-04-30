import uuid
import logging

from django.db import models
from django.utils.translation import gettext_lazy as _

from blog.models.category import Category
from blog.models.timestamp import Timestamp


class About(Timestamp):
    text = models.TextField(
        verbose_name=_("About Blog"),
        unique=True,
        null=True,
        blank=False,
    )

    def __str__(self):
        return f"{self.text[:30]}"

    class Meta:
        ordering = ["-pk"]
