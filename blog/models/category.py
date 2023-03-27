from django.db import models
from django.utils.translation import gettext_lazy as _ # noqa
from blog.models.timestamp import (
    Timestamp,
)

class Category(Timestamp):
    name = models.CharField(
        max_length=200,
        verbose_name=_("Name"),
        unique=True,
        null=True,
        blank=False,
    )
    
    
    def __str__(self):
        return self.name
        