# Generated by Django 2.2.6 on 2020-04-25 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenido', '0008_auto_20200424_2304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peliculas',
            name='anio',
            field=models.CharField(blank=True, editable=False, max_length=4, null=True),
        ),
    ]