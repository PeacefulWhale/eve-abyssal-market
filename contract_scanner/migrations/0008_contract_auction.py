# Generated by Django 2.0.5 on 2018-08-28 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contract_scanner', '0007_contract_location_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='auction',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
