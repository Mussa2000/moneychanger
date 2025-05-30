# Generated by Django 5.1.8 on 2025-05-05 15:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("exchange_rate", "0002_currency_country"),
    ]

    operations = [
        migrations.AddField(
            model_name="currency",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name="exchangerate",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name="exchangesource",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
