# Generated by Django 4.1 on 2023-12-14 20:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("servico", "0003_alter_servico_options_remove_servico_categoria_and_more"),
        ("avaliacao", "0002_remove_avaliacao_usuariocliente_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="avaliacao",
            options={"verbose_name": "Avaliação", "verbose_name_plural": "Avaliações"},
        ),
        migrations.RemoveField(
            model_name="avaliacao",
            name="avaliacao_servico",
        ),
        migrations.AddField(
            model_name="avaliacao",
            name="avaliacao_servico",
            field=models.ManyToManyField(to="servico.servico"),
        ),
    ]
