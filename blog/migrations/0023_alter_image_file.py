# Generated by Django 3.2 on 2023-03-31 20:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0022_alter_image_file"),
    ]

    operations = [
        migrations.AlterField(
            model_name="image",
            name="file",
            field=models.ImageField(null=True, upload_to="blog/images/"),
        ),
    ]
