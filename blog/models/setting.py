from django.db import models
from django.utils.translation import gettext_lazy as _
from blog.models.timestamp import Timestamp


class Setting(Timestamp):
    THEMES = (
        ('dark', 'Dark'),
        ('light', 'Light'),
    )
    theme = models.CharField(
        max_length=200,
        choices=THEMES,
        default='dark',
        null=True,
        blank=True,
        unique=True,
    )
    default_category = models.OneToOneField(
        verbose_name=_("Default Category"),
        to='blog.Category',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    
    def __str__(self):
        return 'settings'

    