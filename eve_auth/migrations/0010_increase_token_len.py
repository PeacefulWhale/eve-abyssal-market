# Generated by Django 2.2.3 on 2019-07-18 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("eve_auth", "0009_evedata"),
    ]

    operations = [
        migrations.AlterField(
            model_name="eveuser",
            name="access_token",
            field=models.CharField(max_length=8192),
        ),
        migrations.AlterField(
            model_name="eveuser",
            name="refresh_token",
            field=models.CharField(max_length=8192),
        ),
    ]
