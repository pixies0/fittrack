from django import forms


class LoginForm(forms.Form):
    email = forms.EmailField(
        label="E-mail",
    )

    password = forms.CharField(
        label="Senha",
        widget=forms.PasswordInput,
    )

    lembrar_me = forms.BooleanField(
        label="Lembrar-me",
        required=False,
    )
