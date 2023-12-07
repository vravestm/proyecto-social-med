from django.db import models

import random
import string
from datetime import date
#
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


def rand_slug():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))


class CustomAccountManager(BaseUserManager):
    def create_user(self, email, nombre, apellido, password, **other_fields):

        if not email:
            raise ValueError(_('Debes ingresar un email.'))

        email = self.normalize_email(email)
        user = self.model(email=email, nombre=nombre,
                          apellido=apellido, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, nombre, apellido, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, nombre, apellido, password, **other_fields)


class UserProfile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField(default=date(1900, 1, 1))
    password = models.CharField(max_length=100)
    telefono = models.IntegerField(default=0)
    nacionalidad = models.CharField(max_length=100, default="")
    ciudad = models.CharField(max_length=100, default="")
    profile_pic = models.ImageField(
        upload_to='users/', default='users/usuario.png')
    ocupacion = models.CharField(max_length=100, default="")

    slug = models.SlugField(max_length=255, unique=True)
    register_date = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre', 'apellido']

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

    def save(self, *args, **kwargs):
        if not self.slug:
            # Si rand_slug() es None, utiliza una cadena vacía

           # print(self.email)
           # print(rand_slug())
            rand_slug_value = rand_slug() or ""
           # print(rand_slug_value)
            self.slug = slugify(rand_slug_value + "-" + self.email)
        super(UserProfile, self).save(*args, **kwargs)
