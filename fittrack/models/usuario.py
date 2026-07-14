from django.contrib.auth.models import AbstractUser
from django.db import models

from fittrack.constants import Grupos

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

    # =====================================================
    # PROPRIEDADES
    # =====================================================

    @property
    def grupo(self):
        """
        Retorna o primeiro grupo do usuário.
        """

        grupo = self.groups.first()

        return grupo.name if grupo else None

    @property
    def is_admin(self):
        """
        Verifica se o usuário é administrador.
        """

        return (
            self.is_superuser or self.groups.filter(name=Grupos.ADMINISTRADOR).exists()
        )

    @property
    def is_professor(self):
        """
        Verifica se o usuário é professor.
        """

        return self.groups.filter(name=Grupos.PROFESSOR).exists()

    @property
    def is_aluno(self):
        """
        Verifica se o usuário é aluno.
        """

        return self.groups.filter(name=Grupos.ALUNO).exists()

    @property
    def perfil(self):
        """
        Retorna o objeto de domínio associado ao usuário.
        """

        if self.is_aluno:
            return getattr(self, "aluno", None)

        if self.is_professor:
            return getattr(self, "professor", None)

        return None
