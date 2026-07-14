from django.db import models

from .usuario import Usuario


class Aluno(models.Model):
    usuario = models.OneToOneField(
        Usuario,
        on_delete=models.CASCADE,
        related_name="aluno",
    )

    data_nascimento = models.DateField()

    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.usuario.nome

    def consultar_treinos(self):
        return self.treinos.all()

    def consultar_avaliacoes(self):
        return self.avaliacoes.all()
