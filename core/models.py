from django.db import models
# aca se importa el username interno de django
from django.contrib.auth.models import User
from datetime import datetime
from users.models import UserProfile


class Usuarios(models.Model):
    username = models.OneToOneField(
        UserProfile, verbose_name="username", on_delete=models.CASCADE, null=False)
    nombre = models.CharField(max_length=40, verbose_name="Nombre", null=False)
    apellido = models.CharField(
        max_length=40, verbose_name="Apellidos", default="Apellido", null=False)
    nac = models.DateField(verbose_name="Fecha de Nacimiento",
                           default=datetime.now, null=False)
    zona = models.CharField(
        max_length=20, verbose_name="Ciudad", default='zona', null=False)
    correo = models.EmailField(
        max_length=30, verbose_name="Direccion de correo", null=False)
    telefono = models.CharField(
        max_length=20, verbose_name="Numero Telefonico", null=False)
    imagen = models.ImageField(
        upload_to='media/', verbose_name="Imagen", null=True)
    trabajo = models.CharField(
        max_length=30, verbose_name="Ocupacion", default="Ocupacion", null=False)

    def __str__(self):
        return str(self.username)

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
