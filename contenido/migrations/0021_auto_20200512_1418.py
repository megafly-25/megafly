# Generated by Django 2.2.6 on 2020-05-12 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenido', '0020_auto_20200508_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='capitulos',
            name='descripcion',
            field=models.CharField(max_length=1500, verbose_name='Descripcion:'),
        ),
    ]
