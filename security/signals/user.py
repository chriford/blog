from django.db.models import Q
from django.dispatch import receiver
from django.db.models.signals import (
    post_save,
    pre_save,
)

from django.db.models.signals import (
    post_save,
    pre_save,
)
from django.db.models import Q
from django.dispatch import receiver

from security.models import (
    User,
    Profile,
)


def user_profile_validator(user, profile):
    if not user.profile:
        user.profile = profile
        user.save()
        return
    return


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, *args, **kwargs):
    if created:
        user_profile = Profile.objects.create(
            user_id=instance.pk,
            email=instance.email,
        )
        user_profile_validator(user=instance, profile=user_profile)
        print("\nuser profile created successfully\n")


# @receiver(pre_save, sender=User)
# def update_user_profile(sender, instance, *args, **kwargs):
#     email = instance.email
#     if email:
#         email = email
#     else:
#         email = None
#     user_profile = Profile.objects.filter(
#         Q(email=instance.email) & Q(user_id =instance.pk)
#     )

#     if user_profile.count().__eq__(1):
#         user_profile = user_profile.first()
#         user_profile.email = email
#         user_profile.save()
#         user_profile_validator(user=instance, profile=user_profile)
#         print('\nuser profile updated successfully\n')
#     elif user_profile.count().__eq__(0):
#         user_profile = Profile.objects.create(user_id=instance.pk, email=email)
#         user_profile_validator(user=instance, profile=user_profile)
#         print('\nuser profile created successfully\n')
#     else:
#         print('\n Nothing happend because you have too many profiles\n')
