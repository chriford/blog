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
def post_update(sender, instance, **kwargs):
    post_count = sender.objects.count()
    print('is deleted status'.capitalize())
    print('kwargs'.capitalize(), kwargs)
    print('post count'.capitalize(), post_count)
    print('instance'.capitalize(), instance)
    # if is_deleted_status:
    #     instance.delete_on = datetime.timedelta(weeks=4, days=2),
    # else:
    #     instance.delete_on = None
    