from django.contrib.auth.models import Group


class GrupoService:
    @staticmethod
    def obter(nome):

        grupo, _ = Group.objects.get_or_create(name=nome)

        return grupo

    @staticmethod
    def adicionar(usuario, nome):

        grupo = GrupoService.obter(nome)

        usuario.groups.add(grupo)

    @staticmethod
    def remover(usuario, nome):

        grupo = GrupoService.obter(nome)

        usuario.groups.remove(grupo)

    @staticmethod
    def pertence(usuario, nome):

        return usuario.groups.filter(name=nome).exists()
