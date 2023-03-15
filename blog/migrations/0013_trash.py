# Generated by Django 3.2 on 2023-03-15 20:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0012_setting'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trash',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated at')),
                ('post_id', models.PositiveIntegerField(null=True)),
                ('title', models.CharField(help_text='Title of the post', max_length=200, null=True, verbose_name='Title')),
                ('body', models.TextField(null=True, verbose_name='Body')),
                ('restore', models.BooleanField(default=False)),
                ('deleted_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(help_text='Select the category of this post', null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.category')),
                ('owner', models.ForeignKey(blank=True, help_text='The owner of this post.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]