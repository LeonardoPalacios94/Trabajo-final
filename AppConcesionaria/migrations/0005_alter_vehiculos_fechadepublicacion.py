# Generated by Django 4.1 on 2022-09-16 00:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppConcesionaria', '0004_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculos',
            name='fechaDePublicacion',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
