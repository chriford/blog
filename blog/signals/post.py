import datetime 

from django.db.models import Q
from django.dispatch import receiver
from django.db.models.signals import (
    post_save,
    pre_save,
    pre_delete,
)
from blog.models import (
    Post,
    Trash,
)


@receiver(pre_save, sender=Post)
def post_update(sender, instance, update_fields, **kwargs):
    post_count = sender.objects.count()
    is_deleted_status: bool = update_fields.get('is_deleted')
    print(is_deleted_status)
    print(kwargs)
    print(instance)
    # if is_deleted_status:
    #     instance.delete_on = datetime.timedelta(weeks=4, days=2),
    # else:
    #     instance.delete_on = None
    