# Generated by Django 5.0.1 on 2024-12-03 19:10

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0010_remove_banner_sub_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="banner",
            name="title",
            field=tinymce.models.HTMLField(),
        ),
    ]