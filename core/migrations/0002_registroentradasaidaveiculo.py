# Generated by Django 4.2.11 on 2024-08-15 21:35

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="RegistroEntradaSaidaVeiculo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "horario_entrada",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                ("horario_saida", models.DateTimeField(blank=True, null=True)),
                (
                    "veiculo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.veiculo"
                    ),
                ),
            ],
        ),
    ]
