# Generated by Django 2.0.9 on 2018-11-19 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("abyssal_modules", "0008_moduledogmaattribute_short_name"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="moduledogmaattribute",
            name="icon_id",
        ),
    ]
