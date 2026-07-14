from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, RedirectView

from fittrack.forms.autenticacao import LoginForm
from fittrack.services.autenticacao_service import AutenticacaoService


class UsuarioLoginView(FormView):
    template_name = "registration/login.html"

    form_class = LoginForm

    success_url = reverse_lazy("dashboard")

    def dispatch(self, request, *args, **kwargs):

        if request.user.is_authenticated:
            return redirect(self.get_success_url())

        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):

        usuario = AutenticacaoService.autenticar(
            email=form.cleaned_data["email"],
            password=form.cleaned_data["password"],
        )

        if usuario is None:
            messages.error(self.request, "E-mail ou senha inválidos.")

            return self.form_invalid(form)

        AutenticacaoService.login(
            request=self.request,
            usuario=usuario,
            lembrar_me=form.cleaned_data["lembrar_me"],
        )

        messages.success(self.request, f"Bem-vindo, {usuario.nome}!")

        return super().form_valid(form)


class UsuarioLogoutView(RedirectView):
    pattern_name = "login"

    def get(self, request, *args, **kwargs):

        AutenticacaoService.logout(request)

        messages.success(request, "Sessão encerrada com sucesso.")

        return super().get(request, *args, **kwargs)
