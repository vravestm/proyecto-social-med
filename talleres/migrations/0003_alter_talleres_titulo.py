# Generated by Django 4.1 on 2023-12-06 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talleres', '0002_talleres_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='talleres',
            name='titulo',
            field=models.CharField(max_length=200, verbose_name='Nombre del taller'),
        ),
    ]
