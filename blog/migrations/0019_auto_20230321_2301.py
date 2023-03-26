# Generated by Django 3.2 on 2023-03-21 23:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0018_alter_like_liker'),
    ]

    operations = [
        migrations.CreateModel(
            name='Voke',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated at')),
                ('upvoke', models.PositiveIntegerField(blank=True, default=0, help_text='Upvoke or like count', null=True, verbose_name='Upvoke')),
                ('downvoke', models.PositiveIntegerField(blank=True, default=0, help_text='Downvoke or diskike count', null=True, verbose_name='Downvoke')),
                ('is_liked', models.BooleanField(default=False)),
                ('is_disliked', models.BooleanField(default=False)),
                ('is_neutral', models.BooleanField(default=True)),
                ('user', models.OneToOneField(blank=True, help_text='The owner of this like.', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]
