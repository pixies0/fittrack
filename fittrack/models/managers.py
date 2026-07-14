from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import Group
from django.db import transaction

from fittrack.constants import Grupos


class UsuarioManager(BaseUserManager):
    use_in_migrations = True

    @transaction.atomic
    def create_user(self, email, password=None, **extra_fields):
        """
        Cria um usuário comum.
        """

        if not email:
            raise ValueError("O e-mail é obrigatório.")

        email = self.normalize_email(email)

        usuario = self.model(
            email=email,
            **extra_fields,
        )

        usuario.set_password(password)

        usuario.save(using=self._db)

        return usuario

    @transaction.atomic
    def create_superuser(self, email, password=None, **extra_fields):
        """
        Cria um superusuário.
        """

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser precisa ter is_staff=True.")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser precisa ter is_superuser=True.")

        usuario = self.create_user(
            email=email,
            password=password,
            **extra_fields,
        )

        grupo, _ = Group.objects.get_or_create(name=Grupos.ADMINISTRADOR)

        usuario.groups.add(grupo)

        return usuario
