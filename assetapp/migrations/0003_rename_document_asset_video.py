# Generated by Django 5.0.6 on 2024-06-19 11:23

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("assetapp", "0002_alter_asset_document"),
    ]

    operations = [
        migrations.RenameField(
            model_name="asset",
            old_name="document",
            new_name="video",
        ),
    ]
