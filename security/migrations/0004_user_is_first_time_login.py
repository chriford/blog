# Generated by Django 3.2 on 2023-03-27 18:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("security", "0003_auto_20230314_0721"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="is_first_time_login",
            field=models.BooleanField(
                blank=True, default=True, verbose_name="is first time login"
            ),
        ),
    ]
