# Generated by Django 3.2 on 2023-03-27 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_auto_20230321_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=200, null=True, unique=True, verbose_name='Name'),
        ),
    ]
