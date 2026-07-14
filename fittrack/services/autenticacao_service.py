from django.contrib.auth import authenticate, login, logout


class AutenticacaoService:
    @staticmethod
    def autenticar(email, password):
        """
        Autentica um usuário utilizando e-mail e senha.
        """

        return authenticate(
            username=email,
            password=password,
        )

    @staticmethod
    def login(request, usuario, lembrar_me=False):
        """
        Efetua o login do usuário.
        """

        login(request, usuario)

        if not lembrar_me:
            request.session.set_expiry(0)

    @staticmethod
    def logout(request):
        """
        Efetua o logout.
        """

        logout(request)
