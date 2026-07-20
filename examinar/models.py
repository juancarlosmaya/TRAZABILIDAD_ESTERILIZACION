from django.db import models

# Create your models here.

class Registro(models.Model):
    numero = models.IntegerField()
    fecha = models.DateTimeField()
    documento = models.FileField(upload_to='')
