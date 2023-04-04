import uuid
import logging

from django.db import models
from django.utils.translation import gettext_lazy as _

from blog.models.timestamp import Timestamp

class Image(Timestamp): 
    file = models.ImageField(
        verbose_name=_("Head Image"),
        upload_to='blog/%H-%M-%S/%Y-%m-%d/',
        null=True,
        blank=False,
    )
    post = models.OneToOneField(
        verbose_name=_("Post"),
        to='blog.Post',
        on_delete=models.CASCADE,
        null=True,
        blank=False,
    )
    
    def __str__(self):
        return f"{self.post.title}"

    def delete(self, *args, **kwargs):
        import os
        from django.conf import settings
        if self.file:
            try:
                self.file.delete()
            except ValueError:
                pass
        self.post.is_active = False
        self.post.save()
        return super().delete(*args, **kwargs)