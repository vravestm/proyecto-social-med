from django.utils import timezone
from django.db import models
# aca se importa el username interno de django
from django.contrib.auth.models import User
from datetime import datetime
from users.models import UserProfile


class Cursos(models.Model):
    titulo = models.CharField(max_length=80, verbose_name="Nombre del curso")
    presentacion = models.TextField(verbose_name="Presentación del curso")
    image = models.ImageField(
        upload_to='media/', verbose_name="Imagen", default='assets/default.jpg', null=True)
    competencias = models.TextField(
        verbose_name="Competencias que vas a adquirir")
    objetivos = models.TextField(verbose_name="Objetivo")
    dirigido = models.TextField(verbose_name="Dirigido a")
    mod_dur_valor = models.TextField(
        verbose_name="Modalidad, duración y valor")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        ordering = ["-created"]

    # para que en el admin se le coloquen los titulos de las noticias
    def __str__(self):
        return self.titulo


class Inscripcion(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(
        verbose_name="Fecha de inscripcion", default=timezone.now, blank=True)
    user = models.ForeignKey(
        UserProfile, verbose_name="Usuario", on_delete=models.CASCADE, null=False)
    curso = models.ForeignKey(
        Cursos, verbose_name="Curso", on_delete=models.CASCADE, null=False)

    def __str__(self):
        return str(self.curso)

    class Meta:
        verbose_name = "Inscripcion"
        verbose_name_plural = "Inscripciones"


class Comentario(models.Model):
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)
    calificacion = models.IntegerField()
    comentario = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.nombre} - {self.fecha_publicacion}'
