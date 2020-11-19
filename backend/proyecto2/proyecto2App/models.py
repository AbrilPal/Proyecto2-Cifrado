from django.db import models

class Login(models.Model):
    usuario = models.CharField(max_length=70, blank=False, default='')
    clave = models.CharField(max_length=200,blank=False, default='')

class Registro(models.Model):
    nombres = models.CharField(max_length=200, blank=False, default='')
    apellidos = models.CharField(max_length=200, blank=False, default='')
    usuario = models.CharField(max_length=70, blank=False, default='')
    clave = models.CharField(max_length=200,blank=False, default='')

class Documento(models.Model):
    dochash = models.CharField(max_length=4000, blank=False, default='')
    codigo = models.CharField(max_length=4000, blank=False, default='')
    

