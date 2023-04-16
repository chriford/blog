import uuid
import logging

from django.db import models
from django.utils.translation import gettext_lazy as _

from blog.models.timestamp import Timestamp


class Trash(Timestamp):
    post_id = models.PositiveIntegerField(null=True, blank=False)
    owner = models.ForeignKey(
        "security.User",
        related_name="owner",
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
    restore = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return f"{self.post.title} - trash-{self.pk}"

    class Meta:
        ordering = ["-pk"]
