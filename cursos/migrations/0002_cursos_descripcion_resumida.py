# Generated by Django 2.2.6 on 2020-05-14 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cursos',
            name='descripcion_resumida',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Descripcion:'),
        ),
    ]
