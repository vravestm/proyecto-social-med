# Generated by Django 4.1 on 2023-12-07 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(default='users/usuario.png', upload_to='users/'),
        ),
    ]