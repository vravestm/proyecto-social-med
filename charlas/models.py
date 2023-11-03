from django.db import models


class Charlas(models.Model):
    titulo = models.CharField(
        max_length=80, verbose_name="Nombre de la charla")
    presentacion = models.TextField(verbose_name="Presentación de la charla")
    competencias = models.TextField(
        verbose_name="Competencias que vas a adquirir")
    objetivos = models.TextField(verbose_name="Objetivos ")
    dirigido = models.TextField(verbose_name="Dirigido a")
    mod_dur_valor = models.TextField(
        verbose_name="Modalidad, duracion y valor")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Charla"
        verbose_name_plural = "Charlas"
        ordering = ["-created"]

    # para que en el admin se le coloquen los titulos de las noticias
    def __str__(self):
        return self.title
