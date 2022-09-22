# Generated by Django 4.1 on 2022-09-22 21:24

import ckeditor.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('AppMensajes', '0006_enviarmensaje_delete_mensajes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enviarmensaje',
            old_name='lastname',
            new_name='apellido',
        ),
        migrations.RenameField(
            model_name='enviarmensaje',
            old_name='name',
            new_name='nombre',
        ),
        migrations.RemoveField(
            model_name='enviarmensaje',
            name='message',
        ),
        migrations.RemoveField(
            model_name='enviarmensaje',
            name='subject',
        ),
        migrations.AddField(
            model_name='enviarmensaje',
            name='fecha',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='enviarmensaje',
            name='mensaje',
            field=ckeditor.fields.RichTextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]