# Generated by Django 2.2.6 on 2020-05-06 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenido', '0017_capitulos'),
    ]

    operations = [
        migrations.RenameField(
            model_name='capitulos',
            old_name='slug_temporada',
            new_name='slug_capitulo',
        ),
    ]
