# Generated by Django 4.1 on 2023-12-07 02:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cursos', '0004_alter_inscripcion_date_alter_inscripcion_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscripcion',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
    ]
