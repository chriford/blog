from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import PermissionsMixin, AbstractUser, AbstractBaseUser
from security.manager import CustomUserManager

class User(AbstractBaseUser, PermissionsMixin):
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
    first_name = models.CharField(
        verbose_name=_('first_name'),
        max_length=255,
        null=True,
    )
    last_name = models.CharField(
        verbose_name=_('Last name'),
        max_length=255,
        null=True,
    )
    phone_number = models.CharField(
        verbose_name=_('Phone number'),
        max_length=15,
        null=True,
        blank=True,
    )
    country = models.CharField(
        verbose_name=_('Country'),
        max_length=25,
        null=True,
        blank=True,
    )
    state = models.CharField(
        verbose_name=_('State/Province'),
        max_length=15,
        null=True,
        blank=True,
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
    postal_code = models.CharField(
        verbose_name=_('Postal code'),
        max_length=10,
        null=True,
        blank=True,
    )
    is_first_time_login = models.BooleanField(
        verbose_name=_("is first time login"),
        default=True,
        blank=True,
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
        to='security.Profile',
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
