# Generated by Django 4.1 on 2023-11-14 18:25

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cursos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inscripcion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='Fecha de inscripcion')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cursos.cursos', verbose_name='Curso')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Inscripcion',
                'verbose_name_plural': 'Inscripciones',
            },
        ),
    ]