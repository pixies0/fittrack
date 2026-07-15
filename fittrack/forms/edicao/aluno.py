from django import forms

from fittrack.models import Aluno
from fittrack.services.usuario_service import UsuarioService


class AlunoUpdateForm(forms.Form):
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

    data_nascimento = forms.DateField(
        label="Data de Nascimento",
        widget=forms.DateInput(
            attrs={
                "type": "date",
            }
        ),
    )

    ativo = forms.BooleanField(
        label="Ativo",
        required=False,
    )

    def __init__(self, *args, instance: Aluno = None, **kwargs):

        self.instance = instance

        super().__init__(*args, **kwargs)

        if self.instance:
            self.fields["nome"].initial = instance.usuario.nome
            self.fields["cpf"].initial = instance.usuario.cpf
            self.fields["email"].initial = instance.usuario.email
            self.fields["telefone"].initial = instance.usuario.telefone

            self.fields["data_nascimento"].initial = instance.data_nascimento

            self.fields["ativo"].initial = instance.ativo

    def save(self):

        return UsuarioService.atualizar_aluno(
            aluno=self.instance,
            nome=self.cleaned_data["nome"],
            cpf=self.cleaned_data["cpf"],
            email=self.cleaned_data["email"],
            telefone=self.cleaned_data["telefone"],
            data_nascimento=self.cleaned_data["data_nascimento"],
            ativo=self.cleaned_data["ativo"],
        )
