from django.contrib.auth.models import AbstractUser
from django.db import models

from .managers import UsuarioManager


class Usuario(AbstractUser):
    username = None

    nome = models.CharField(
        "Nome",
        max_length=150,
    )

    email = models.EmailField(
        "E-mail",
        unique=True,
    )

    cpf = models.CharField(
        "CPF",
        max_length=14,
        unique=True,
    )

    telefone = models.CharField(
        "Telefone",
        max_length=20,
        blank=True,
    )

    foto = models.ImageField(
        "Foto",
        upload_to="usuarios/",
        blank=True,
        null=True,
    )

    objects = UsuarioManager()

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = [
        "nome",
        "cpf",
    ]

    def __str__(self):
        return self.nome
