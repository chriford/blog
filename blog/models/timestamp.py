from django.db import models
from django.utils.translation import gettext_lazy as _

class Timestamp(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Created at'),
        null=True,
        blank=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_('Updated at'),
        null=True,
        blank=True,
    )

    class Meta:
        abstract = True
