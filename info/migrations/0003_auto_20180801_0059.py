# Generated by Django 2.0 on 2018-08-01 05:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0002_auto_20180801_0053'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidato',
            name='fecha_inicio_politica',
        ),
        migrations.RemoveField(
            model_name='candidato',
            name='fecha_nacimiento',
        ),
        migrations.AddField(
            model_name='candidato',
            name='fecha_in_polt',
            field=models.DateField(default=datetime.date.today, verbose_name='Fecha de inicio en la política'),
        ),
        migrations.AddField(
            model_name='candidato',
            name='fecha_nac',
            field=models.DateField(default=datetime.date.today, verbose_name='Fecha de nacimiento'),
        ),
    ]
