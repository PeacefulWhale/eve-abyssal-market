# Generated by Django 2.0.5 on 2018-06-04 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("eve_auth", "0003_store_auth_tokens"),
    ]

    operations = [
        migrations.AddField(
            model_name="eveuser",
            name="scope_read_assets",
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
