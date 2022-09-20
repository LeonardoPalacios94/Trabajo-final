from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

class Mensajes(models.Model):
    titulo=models.CharField(max_length=40, default="Mensaje")
    remitente=models.ForeignKey(User, on_delete=models.CASCADE, related_name='remitente')
    recibido=models.ForeignKey(User, on_delete=models.CASCADE, related_name='recibido')
    mensaje=models.CharField(max_length=1200)
    fecha=models.DateTimeField(default=datetime.datetime.now)
   

    def __str__(self):
        return self.mensaje

    class Meta:
        ordering = ('fecha',)