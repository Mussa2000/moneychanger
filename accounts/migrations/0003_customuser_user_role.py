# Generated by Django 5.1.8 on 2025-05-06 03:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0002_remove_customuser_is_farmer"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="user_role",
            field=models.CharField(
                choices=[("Trader", "Trader"), ("Regulator", "Regulator")],
                default="Trader",
                max_length=50,
            ),
        ),
    ]
