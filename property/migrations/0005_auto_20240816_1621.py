# Generated by Django 2.2.24 on 2024-08-16 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("property", "0004_auto_20240816_1608"),
    ]

    operations = [
        migrations.AlterField(
            model_name="flat",
            name="new_building",
            field=models.BooleanField(
                db_index=True, default=None, null=True, verbose_name="Новостройка?"
            ),
        ),
    ]
