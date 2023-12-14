# Generated by Django 4.1 on 2023-12-14 19:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("categoria", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="categoria",
            name="nome",
        ),
        migrations.RemoveField(
            model_name="categoria",
            name="taxa_padrao",
        ),
        migrations.AddField(
            model_name="categoria",
            name="modo_de_atendimento",
            field=models.CharField(
                blank=True, max_length=100, verbose_name="Modo de Atendimento"
            ),
        ),
        migrations.AddField(
            model_name="categoria",
            name="ramo_de_negocio",
            field=models.CharField(
                blank=True, max_length=100, verbose_name="Ramo do Negócio"
            ),
        ),
        migrations.AlterField(
            model_name="categoria",
            name="descricao",
            field=models.TextField(blank=True, verbose_name="Descrição"),
        ),
    ]