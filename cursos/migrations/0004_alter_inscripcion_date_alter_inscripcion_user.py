# Generated by Django 4.1 on 2023-12-07 02:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cursos', '0003_comentario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscripcion',
            name='date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Fecha de inscripcion'),
        ),
        migrations.AlterField(
            model_name='inscripcion',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True, verbose_name='Usuario'),
        ),
    ]
