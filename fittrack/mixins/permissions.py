from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import AccessMixin
from fittrack.constants import Grupos


class LoginRequiredMixin(AccessMixin):
    """
    Exige que o usuário esteja autenticado.
    """

    login_url = "login"

    def dispatch(self, request, *args, **kwargs):

        if not request.user.is_authenticated:
            return self.handle_no_permission()

        return super().dispatch(request, *args, **kwargs)


class GroupRequiredMixin(LoginRequiredMixin):
    """
    Exige que o usuário pertença a um ou mais grupos.
    """

    groups_required = None

    def has_group_permission(self):

        if not self.groups_required:
            raise ValueError("Defina 'groups_required' no mixin.")

        return self.request.user.groups.filter(name__in=self.groups_required).exists()

    def dispatch(self, request, *args, **kwargs):

        response = super().dispatch(request, *args, **kwargs)

        if not request.user.is_authenticated:
            return response

        if not self.has_group_permission():
            raise PermissionDenied(
                "Você não possui permissão para acessar este recurso."
            )

        return response


class AdministradorRequiredMixin(GroupRequiredMixin):
    groups_required = [
        Grupos.ADMINISTRADOR,
    ]


class ProfessorRequiredMixin(GroupRequiredMixin):
    groups_required = [
        Grupos.PROFESSOR,
    ]


class AlunoRequiredMixin(GroupRequiredMixin):
    groups_required = [
        Grupos.ALUNO,
    ]


class AdministradorOuProfessorRequiredMixin(GroupRequiredMixin):
    groups_required = [
        Grupos.ADMINISTRADOR,
        Grupos.PROFESSOR,
    ]


class AdministradorOuAlunoRequiredMixin(GroupRequiredMixin):
    groups_required = [
        Grupos.ADMINISTRADOR,
        Grupos.ALUNO,
    ]


class UsuarioSistemaRequiredMixin(GroupRequiredMixin):
    groups_required = [
        Grupos.ADMINISTRADOR,
        Grupos.PROFESSOR,
        Grupos.ALUNO,
    ]
