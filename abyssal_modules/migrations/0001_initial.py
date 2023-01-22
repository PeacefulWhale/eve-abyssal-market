# Generated by Django 2.0 on 2018-08-23 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("contract_scanner", "0002_contract_knowledge"),
    ]

    operations = [
        migrations.CreateModel(
            name="EveCharacter",
            fields=[
                ("id", models.BigIntegerField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name="Module",
            fields=[
                ("id", models.BigIntegerField(primary_key=True, serialize=False)),
                ("mutator_type_id", models.IntegerField()),
                ("source_type_id", models.IntegerField()),
                ("first_seen", models.DateTimeField(auto_now_add=True, db_index=True)),
            ],
        ),
        migrations.CreateModel(
            name="ModuleAttribute",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("value", models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name="ModuleDogmaAttribute",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=64)),
                ("high_is_good", models.NullBooleanField()),
                ("icon_id", models.IntegerField()),
                ("unit_str", models.CharField(max_length=16)),
                ("interesting", models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name="ModuleType",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=128)),
                (
                    "attributes",
                    models.ManyToManyField(
                        related_name="_moduletype_attributes_+",
                        to="abyssal_modules.ModuleDogmaAttribute",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="OwnershipRecord",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("start", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("end", models.DateTimeField(db_index=True, null=True)),
                (
                    "asset_owner",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="abyssal_modules.EveCharacter",
                    ),
                ),
                (
                    "contract_contract",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="contract_scanner.Contract",
                    ),
                ),
                (
                    "module",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="abyssal_modules.Module",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="moduleattribute",
            name="attribute",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="abyssal_modules.ModuleDogmaAttribute",
            ),
        ),
        migrations.AddField(
            model_name="moduleattribute",
            name="module",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="abyssal_modules.Module"
            ),
        ),
        migrations.AddField(
            model_name="module",
            name="attributes",
            field=models.ManyToManyField(
                related_name="_module_attributes_+",
                through="abyssal_modules.ModuleAttribute",
                to="abyssal_modules.ModuleDogmaAttribute",
            ),
        ),
        migrations.AddField(
            model_name="module",
            name="creator",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="creations",
                to="abyssal_modules.EveCharacter",
            ),
        ),
        migrations.AddField(
            model_name="module",
            name="type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="modules",
                to="abyssal_modules.ModuleType",
            ),
        ),
    ]
