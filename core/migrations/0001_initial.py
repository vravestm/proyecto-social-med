# Generated by Django 4.1 on 2023-11-29 19:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40, verbose_name='Nombre')),
                ('apellido', models.CharField(default='Apellido', max_length=40, verbose_name='Apellidos')),
                ('nac', models.DateField(default=datetime.datetime.now, verbose_name='Fecha de Nacimiento')),
                ('zona', models.CharField(default='zona', max_length=20, verbose_name='Ciudad')),
                ('correo', models.EmailField(max_length=30, verbose_name='Direccion de correo')),
                ('telefono', models.CharField(max_length=20, verbose_name='Numero Telefonico')),
                ('imagen', models.ImageField(null=True, upload_to='media/', verbose_name='Imagen')),
                ('trabajo', models.CharField(default='Ocupacion', max_length=30, verbose_name='Ocupacion')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
            },
        ),
    ]
