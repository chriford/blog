from django.db import models
from django.utils.translation import gettext_lazy as _

from blog.models.category import Category
from blog.models.timestamp import Timestamp


class Subscriber(Timestamp):
    user = models.ForeignKey(
        "security.User",
        help_text=_("Subscriber to newsletter"),
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )
    is_subscribed = models.BooleanField(default=False)

    class Meta:
        ordering = ["-pk"]

    def __str__(self):
        return self.user.username