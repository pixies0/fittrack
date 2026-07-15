from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import (
    DeleteView,
    DetailView,
    FormView,
    ListView,
)

from fittrack.services import UsuarioService
from fittrack.constants import Grupos
from fittrack.forms.cadastro import AlunoCreateForm
from fittrack.forms.edicao import AlunoUpdateForm
from fittrack.mixins import (
    GroupRequiredMixin,
    UsuarioSistemaRequiredMixin,
)
from fittrack.models import Aluno


GRUPOS_ADMIN = (Grupos.ADMINISTRADOR,)

GRUPOS_ADMIN_PROFESSOR = (
    Grupos.ADMINISTRADOR,
    Grupos.PROFESSOR,
)


class AlunoListView(
    UsuarioSistemaRequiredMixin,
    GroupRequiredMixin,
    ListView,
):
    model = Aluno
    template_name = "aluno/list.html"
    context_object_name = "alunos"
    grupos_permitidos = GRUPOS_ADMIN_PROFESSOR
    ordering = ("usuario__nome",)
    paginate_by = 10

    def get_queryset(self):
        queryset = Aluno.objects.select_related("usuario")
        pesquisa = self.request.GET.get("q")

        if pesquisa:
            queryset = queryset.filter(usuario__nome__icontains=pesquisa)

        return Aluno.objects.select_related("usuario").prefetch_related(
            "matriculas__plano"
        )


class AlunoCreateView(
    UsuarioSistemaRequiredMixin,
    GroupRequiredMixin,
    FormView,
):
    template_name = "aluno/form.html"
    form_class = AlunoCreateForm
    success_url = reverse_lazy("aluno-list")
    grupos_permitidos = GRUPOS_ADMIN

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context["titulo"] = "Novo Aluno"
        context["botao"] = "Cadastrar"

        return context

    def form_valid(self, form):

        form.save()

        messages.success(
            self.request,
            "Aluno cadastrado com sucesso.",
        )

        return super().form_valid(form)


class AlunoDetailView(
    UsuarioSistemaRequiredMixin,
    GroupRequiredMixin,
    DetailView,
):
    model = Aluno
    template_name = "aluno/detail.html"
    context_object_name = "aluno"
    grupos_permitidos = GRUPOS_ADMIN_PROFESSOR

    def get_queryset(self):
        return Aluno.objects.select_related("usuario")


class AlunoUpdateView(
    UsuarioSistemaRequiredMixin,
    GroupRequiredMixin,
    FormView,
):
    template_name = "aluno/form.html"
    form_class = AlunoUpdateForm
    success_url = reverse_lazy("aluno-list")
    grupos_permitidos = GRUPOS_ADMIN

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["titulo"] = "Editar Aluno"
        context["botao"] = "Salvar Alterações"

        return context

    def get_form_kwargs(self):

        kwargs = super().get_form_kwargs()
        kwargs["instance"] = Aluno.objects.select_related("usuario").get(
            pk=self.kwargs["pk"]
        )
        return kwargs

    def form_valid(self, form):

        form.save()

        messages.success(
            self.request,
            "Aluno atualizado com sucesso.",
        )

        return super().form_valid(form)


class AlunoDeleteView(
    UsuarioSistemaRequiredMixin,
    GroupRequiredMixin,
    DeleteView,
):
    model = Aluno
    template_name = "aluno/delete.html"
    success_url = reverse_lazy("aluno-list")
    grupos_permitidos = GRUPOS_ADMIN

    def get_queryset(self):
        return Aluno.objects.select_related("usuario")

    def post(self, request, *args, **kwargs):

        aluno = self.get_object()

        UsuarioService.remover_aluno(aluno)

        messages.success(
            request,
            "Aluno removido com sucesso.",
        )

        return redirect(self.success_url)
