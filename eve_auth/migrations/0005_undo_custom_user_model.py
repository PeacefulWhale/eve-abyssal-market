# Generated by Django 2.1.3 on 2018-12-01 00:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("eve_auth", "0004_scope_read_assets"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="eveuser",
            name="is_active",
        ),
        migrations.RemoveField(
            model_name="eveuser",
            name="is_admin",
        ),
        migrations.RemoveField(
            model_name="eveuser",
            name="last_login",
        ),
        migrations.RemoveField(
            model_name="eveuser",
            name="password",
        ),
        migrations.RemoveField(
            model_name="eveuser",
            name="scope_read_contracts",
        ),
    ]
