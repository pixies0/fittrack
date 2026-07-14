from django import forms

from fittrack.services.usuario_service import UsuarioService

from fittrack.models import Usuario


class AlunoForm(forms.Form):
    nome = forms.CharField(
        label="Nome",
        max_length=150,
    )

    cpf = forms.CharField(
        label="CPF",
        max_length=14,
    )

    email = forms.EmailField(
        label="E-mail",
    )

    telefone = forms.CharField(
        label="Telefone",
        max_length=20,
    )

    senha = forms.CharField(
        label="Senha",
        min_length=8,
        widget=forms.PasswordInput(render_value=False),
    )

    confirmar_senha = forms.CharField(
        label="Confirmar Senha",
        min_length=8,
        widget=forms.PasswordInput(render_value=False),
    )

    data_nascimento = forms.DateField(
        label="Data de Nascimento",
        widget=forms.DateInput(attrs={"type": "date"}),
    )

    def clean_cpf(self):
        cpf = self.cleaned_data["cpf"]

        if Usuario.objects.filter(cpf=cpf).exists():
            raise forms.ValidationError("Já existe um usuário com este CPF.")

        return cpf

    def clean_email(self):
        email = self.cleaned_data["email"]

        if Usuario.objects.filter(email=email).exists():
            raise forms.ValidationError("Já existe um usuário com este e-mail.")

        return email

    def clean(self):

        cleaned_data = super().clean()

        senha = cleaned_data.get("senha")
        confirmar = cleaned_data.get("confirmar_senha")

        if senha != confirmar:
            raise forms.ValidationError("As senhas não conferem.")

        return cleaned_data

    def save(self, commit=True):

        if not commit:
            raise NotImplementedError("AlunoForm requer commit=True.")

        return UsuarioService.criar_aluno(
            nome=self.cleaned_data["nome"],
            cpf=self.cleaned_data["cpf"],
            email=self.cleaned_data["email"],
            telefone=self.cleaned_data["telefone"],
            data_nascimento=self.cleaned_data["data_nascimento"],
            password=self.cleaned_data["senha"],
        )
