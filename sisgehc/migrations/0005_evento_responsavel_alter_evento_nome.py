# Generated by Django 5.1.1 on 2024-09-17 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sisgehc', '0004_alter_evento_descricao'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='responsavel',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='evento',
            name='nome',
            field=models.CharField(max_length=50),
        ),
    ]