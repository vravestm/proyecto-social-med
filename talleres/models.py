from django.db import models


class Talleres(models.Model):
    titulo = models.CharField(
        max_length=80, verbose_name="Nombre del taller")
    presentacion = models.TextField(verbose_name="Presentación del taller")
    competencias = models.TextField(
        verbose_name="Competencias que vas a adquirir")
    objetivos = models.TextField(verbose_name="Objetivo")
    dirigido = models.TextField(verbose_name="Dirigido a")
    mod_dur_valor = models.TextField(
        verbose_name="Modalidad, duración y valor")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Taller"
        verbose_name_plural = "Talleres"
        ordering = ["-created"]

    # para que en el admin se le coloquen los titulos de las noticias
    def __str__(self):
        return self.titulo
