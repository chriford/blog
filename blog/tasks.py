from __future__ import (
    absolute_import,
    unicode_literals,
)

from celery import shared_task


@shared_task
def send_email(
    to, subject="default message", body="hiiiiiii", from_="siamechrif@gmail.com"
):
    return "Email send to %s" % (to)
