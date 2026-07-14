from django.contrib.auth.models import Group


class GrupoService:
    @staticmethod
    def obter(nome):
        """
        Obtém um grupo existente ou o cria.
        """

        grupo, _ = Group.objects.get_or_create(
            name=nome,
        )

        return grupo

    @staticmethod
    def adicionar(usuario, nome):
        """
        Adiciona um usuário ao grupo.
        """

        grupo = GrupoService.obter(nome)

        usuario.groups.add(grupo)

    @staticmethod
    def remover(usuario, nome):
        """
        Remove um usuário do grupo.
        """

        grupo = GrupoService.obter(nome)

        usuario.groups.remove(grupo)

    @staticmethod
    def substituir(usuario, nome):
        """
        Remove todos os grupos do usuário e adiciona um novo.
        """

        usuario.groups.clear()

        GrupoService.adicionar(
            usuario,
            nome,
        )

    @staticmethod
    def pertence(usuario, nome):
        """
        Verifica se o usuário pertence ao grupo informado.
        """

        return usuario.groups.filter(
            name=nome,
        ).exists()
