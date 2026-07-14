from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError


class SenhaService:
    @staticmethod
    def validar(password, usuario=None):
        """
        Valida a senha utilizando os validadores do Django.
        """

        validate_password(password, usuario)

    @staticmethod
    def alterar(usuario, nova_senha):
        """
        Altera a senha do usuário.
        """

        SenhaService.validar(
            nova_senha,
            usuario,
        )

        usuario.set_password(nova_senha)
        usuario.save(update_fields=["password"])
