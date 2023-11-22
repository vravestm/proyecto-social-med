from django.db import models
from django.contrib.auth.models import User #aca se importa el username interno de django



class Usuarios(models.Model):
    username = models.ForeignKey(User,verbose_name="username",on_delete=models.CASCADE,null=False)
    nombre = models.CharField(max_length=20,verbose_name="Nombre",null=False)
    apellido1 = models.CharField(max_length=20,verbose_name="Primer Apellido",null=False)
    apellido2 = models.CharField(max_length=20,verbose_name="Segundo Apellido",null=False)
    edad = models.IntegerField(verbose_name="Edad",null=False)
    zona = models.CharField(max_length=20,verbose_name="Ciudad",default='zona',null=False)
    correo = models.EmailField(max_length=30,verbose_name="Direccion de correo",null=False)
    telefono = models.CharField(max_length=20,verbose_name="Numero Telefonico",null=False)
    imagen = models.ImageField(upload_to='media/',verbose_name="Imagen", null=True)


    def __str__(self):
        return self.username
    class Meta:
        verbose_name="Usuario"
        verbose_name_plural="Usuarios"



