# Generated by Django 4.1 on 2023-12-14 08:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("categoria", "0001_initial"),
        ("profissional", "0005_remove_profissional_servicosprestados"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profissional",
            name="email",
        ),
        migrations.RemoveField(
            model_name="profissional",
            name="habilidades",
        ),
        migrations.RemoveField(
            model_name="profissional",
            name="nome",
        ),
        migrations.AddField(
            model_name="profissional",
            name="cnpj",
            field=models.CharField(
                default="", max_length=50, unique=True, verbose_name="CNPJ"
            ),
        ),
        migrations.AddField(
            model_name="profissional",
            name="idade",
            field=models.IntegerField(default=0, verbose_name="Idade"),
        ),
        migrations.AddField(
            model_name="profissional",
            name="nome_completo",
            field=models.CharField(
                blank=True, default="", max_length=300, verbose_name="Nome"
            ),
        ),
        migrations.AddField(
            model_name="profissional",
            name="profissional_categoria",
            field=models.ManyToManyField(to="categoria.categoria"),
        ),
        migrations.AlterField(
            model_name="profissional",
            name="telefone",
            field=models.CharField(
                blank=True, default="", max_length=11, verbose_name="Experiência"
            ),
        ),
    ]
