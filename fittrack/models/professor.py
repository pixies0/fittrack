from django.db import models

from .aluno import Aluno
from .usuario import Usuario


class Professor(models.Model):
    usuario = models.OneToOneField(
        Usuario,
        on_delete=models.CASCADE,
        related_name="professor",
    )

    cref = models.CharField(
        max_length=20,
        unique=True,
    )

    especialidade = models.CharField(
        max_length=100,
    )

    def __str__(self):
        return self.usuario.nome

    def listar_treinos(self):
        return self.treinos.all()

    def listar_alunos(self):
        return Aluno.objects.filter(treinos__professor=self).distinct()
