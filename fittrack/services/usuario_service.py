from django.contrib.auth.models import Group
from django.db import transaction

from fittrack.constants import Grupos
from fittrack.models import Aluno, Professor, Usuario
from fittrack.services import GrupoService


class UsuarioService:
    @staticmethod
    def _obter_grupo(nome):
        """
        Obtém um grupo existente ou o cria caso ainda não exista.
        """
        grupo, _ = Group.objects.get_or_create(name=nome)
        return grupo

    @staticmethod
    def _criar_usuario(
        *,
        nome,
        cpf,
        email,
        telefone,
        password,
    ):
        """
        Cria um usuário do sistema.
        """
        return Usuario.objects.create_user(
            email=email,
            password=password,
            nome=nome,
            cpf=cpf,
            telefone=telefone,
        )

    @staticmethod
    @transaction.atomic
    def criar_aluno(
        *,
        nome,
        cpf,
        email,
        telefone,
        data_nascimento,
        password,
    ):
        """
        Cria um usuário do tipo Aluno.
        """

        usuario = UsuarioService._criar_usuario(
            nome=nome,
            cpf=cpf,
            email=email,
            telefone=telefone,
            password=password,
        )

        GrupoService.adicionar(
            usuario,
            Grupos.ALUNO,
        )

        aluno = Aluno.objects.create(
            usuario=usuario,
            data_nascimento=data_nascimento,
            ativo=True,
        )

        return aluno

    @staticmethod
    @transaction.atomic
    def atualizar_aluno(
        *,
        aluno,
        nome,
        cpf,
        email,
        telefone,
        data_nascimento,
        ativo,
    ):
        """
        Atualiza um aluno e seu usuário associado.
        """

        usuario = aluno.usuario

        usuario.nome = nome
        usuario.cpf = cpf
        usuario.email = email
        usuario.telefone = telefone

        usuario.save()

        aluno.data_nascimento = data_nascimento
        aluno.ativo = ativo

        aluno.save()

        return aluno

    @staticmethod
    @transaction.atomic
    def remover_aluno(aluno):
        """
        Remove um aluno e seu usuário associado.
        """

        usuario = aluno.usuario

        usuario.delete()

    @staticmethod
    @transaction.atomic
    def criar_professor(
        *,
        nome,
        cpf,
        email,
        telefone,
        cref,
        especialidade,
        password,
    ):
        """
        Cria um usuário do tipo Professor.
        """

        usuario = UsuarioService._criar_usuario(
            nome=nome,
            cpf=cpf,
            email=email,
            telefone=telefone,
            password=password,
        )

        GrupoService.adicionar(
            usuario,
            Grupos.PROFESSOR,
        )

        professor = Professor.objects.create(
            usuario=usuario,
            cref=cref,
            especialidade=especialidade,
        )

        return professor
