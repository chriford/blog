# Generated by Django 3.2 on 2023-04-03 21:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0006_user_postal_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='country',
        ),
        migrations.RemoveField(
            model_name='user',
            name='postal_code',
        ),
        migrations.RemoveField(
            model_name='user',
            name='state',
        ),
    ]