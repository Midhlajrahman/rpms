# Generated by Django 5.0.1 on 2024-04-17 19:09

import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="team",
            options={
                "ordering": ["order"],
                "verbose_name": "Team",
                "verbose_name_plural": "Teams",
            },
        ),
        migrations.AddField(
            model_name="team",
            name="order",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="servicefaq",
            name="answer",
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
    ]
