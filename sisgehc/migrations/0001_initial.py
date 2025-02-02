# Generated by Django 5.1.1 on 2025-02-02 21:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Aluno",
            fields=[
                ("id_matricula", models.AutoField(primary_key=True, serialize=False)),
                ("nome", models.CharField(max_length=100)),
                ("senha", models.CharField(max_length=50)),
                ("horas_complementares", models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="Coordenador",
            fields=[
                ("id_matricula", models.AutoField(primary_key=True, serialize=False)),
                ("nome", models.CharField(max_length=100)),
                ("senha", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Curso",
            fields=[
                ("id_curso", models.AutoField(primary_key=True, serialize=False)),
                ("nome", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="AtividadeComplementar",
            fields=[
                ("id_atividade", models.AutoField(primary_key=True, serialize=False)),
                ("carga_horaria", models.IntegerField()),
                ("data_submissao", models.DateField()),
                ("data_validacao", models.DateField(blank=True, null=True)),
                ("arquivo_certificacao", models.FileField(upload_to="certificados/")),
                ("tipo_atividade", models.CharField(max_length=100)),
                ("sub_tipo", models.CharField(blank=True, max_length=100, null=True)),
                ("area_de_conhecimento", models.CharField(max_length=100)),
                (
                    "aluno",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="sisgehc.aluno"
                    ),
                ),
                (
                    "coordenador",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="sisgehc.coordenador",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="coordenador",
            name="curso",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="sisgehc.curso"
            ),
        ),
        migrations.AddField(
            model_name="aluno",
            name="curso",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="sisgehc.curso"
            ),
        ),
        migrations.CreateModel(
            name="Evento",
            fields=[
                ("id_evento", models.AutoField(primary_key=True, serialize=False)),
                ("nome", models.CharField(max_length=200)),
                ("tipo", models.CharField(max_length=50)),
                ("horas_complementares", models.IntegerField()),
                ("data_inicio", models.DateField()),
                ("data_encerramento", models.DateField()),
                ("hora_inicio", models.TimeField()),
                ("hora_encerrado", models.TimeField()),
                ("limite_inscricao", models.DateField()),
                ("descricao_evento", models.TextField()),
                (
                    "curso",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="sisgehc.curso"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Inscricao",
            fields=[
                ("id_inscricao", models.AutoField(primary_key=True, serialize=False)),
                ("participacao_boolean", models.BooleanField(default=False)),
                (
                    "porcent_participacao",
                    models.DecimalField(decimal_places=2, max_digits=5),
                ),
                (
                    "aluno",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="sisgehc.aluno"
                    ),
                ),
                (
                    "evento",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="sisgehc.evento"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Presenca",
            fields=[
                ("id_presenca", models.AutoField(primary_key=True, serialize=False)),
                (
                    "inscricao",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="sisgehc.inscricao",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Professor",
            fields=[
                ("id_matricula", models.AutoField(primary_key=True, serialize=False)),
                ("nome", models.CharField(max_length=100)),
                ("senha", models.CharField(max_length=50)),
                (
                    "curso",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="sisgehc.curso"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="evento",
            name="professor",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="sisgehc.professor"
            ),
        ),
    ]
