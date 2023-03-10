import auth.signals
from django.db.models import Q
from django.dispatch import receiver
from django.db.models.signals import (
    post_save,
    pre_save,
)
