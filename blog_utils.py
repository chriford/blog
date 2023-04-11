from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import EmailMessage

from security.models import User, Profile
from security.forms import UserCreationForm
import types


def send_email(
    recipient_list: list = [], subject: str = "Reset Password", body: str = None
) -> None:
    """A custom module for sending email,
    expects parameters:
    recipiet_list: a list of emails where the email will be sent to,
    subject: the title of the email body,
    body: the body of the email.
    """
    subject = subject
    sender = settings.EMAIL_HOST_USER
    recipient_list = list(recipient_list)
    email_template = body
    send_mail(
        subject=subject,
        message=email_template,
        from_email=sender,
        recipient_list=recipient_list,
        fail_silently=False,
    )
    return
    # alternative way of sending an email
    # msg = EmailMessage(subject,
    #     email_template,
    #     to=recipient_list,
    # )
    # msg.send()
