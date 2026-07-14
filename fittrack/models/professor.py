from django.db import models

from .aluno import Aluno


class Professor(models.Model):
    nome = models.CharField(max_length=120)
    cref = models.CharField(max_length=20, unique=True)
    especialidade = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

    def listar_treinos(self):
        return self.treinos.all()

    def listar_alunos(self):
        return Aluno.objects.filter(treinos__professor=self).distinct()
