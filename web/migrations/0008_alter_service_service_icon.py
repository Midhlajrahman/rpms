# Generated by Django 5.0.1 on 2024-12-03 18:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0007_service_service_icon"),
    ]

    operations = [
        migrations.AlterField(
            model_name="service",
            name="service_icon",
            field=models.FileField(upload_to="service_icons/"),
        ),
    ]
