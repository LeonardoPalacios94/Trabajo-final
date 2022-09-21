# Generated by Django 4.1 on 2022-09-20 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppMensajes', '0003_remove_mensajes_esleido_mensajes_titulo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mensajes',
            name='id',
        ),
        migrations.RemoveField(
            model_name='mensajes',
            name='titulo',
        ),
        migrations.AddField(
            model_name='mensajes',
            name='idmensaje',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mensajes',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
