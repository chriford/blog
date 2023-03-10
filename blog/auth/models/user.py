from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import PermissionsMixin, AbstractUser, AbstractBaseUser
from blog.auth.manager import CustomUserManager

class User(models.Model):
    email = models.EmailField(
        verbose_name=_('email address'),
        max_length=255,
        unique=True,
    )
    username = models.CharField(
        verbose_name=_('username'),
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(
        verbose_name=_('active'),
        default=True,
    )
    is_staff = models.BooleanField(
        verbose_name=_('staff status'),
        default=False,
    )
    is_superuser = models.BooleanField(
        verbose_name=_('superuser status'),
        default=False,
    )
    date_joined = models.DateTimeField(
        verbose_name=_('date joined'),
        auto_now_add=True,
    )
    last_login = models.DateTimeField(
        verbose_name=_('last login'),
        auto_now=True,
    )
    profile = models.OneToOneField(
        to='blog.Profile',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    objects = CustomUserManager()
    
    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'         
    REQUIRED_FIELDS = ['email']
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return f"{self.username}|{self.email}"
