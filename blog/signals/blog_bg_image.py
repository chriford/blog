import os
from django.dispatch import receiver
from django.db.models.signals import (
    post_save,
    pre_save,
    pre_delete,
)

from django.dispatch import receiver
from blog.models import (
    Image,
    Post,
)

# @receiver(post_save, sender=Image)
# def activate_blog_post(sender, instance, created, *args, **kwargs):    
#     if created:
#         blog = Post.objects.get(pk=instance.post.pk)
#         blog.is_active = True
#         blog.save()

@receiver(pre_save, sender=Image)
def reactivate_blog_post(sender, instance, *args, **kwargs):    
    blog = Post.objects.filter(
        pk=instance.post.pk, 
        title=instance.post.title,
    ).first()
    print(blog.body)
    blog.is_active = True    
    blog.save()
