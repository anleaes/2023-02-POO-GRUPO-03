# Generated by Django 4.1 on 2023-12-09 22:32

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("localizacao", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="localizacao",
            options={
                "ordering": ["id"],
                "verbose_name": "Local",
                "verbose_name_plural": "Locais",
            },
        ),
    ]
