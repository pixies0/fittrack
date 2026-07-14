from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=120)
    cpf = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    data_nascimento = models.DateField()
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

    def consultar_treinos(self):
        return self.treinos.all()

    def consultar_avaliacoes(self):
        return self.avaliacoes.all()