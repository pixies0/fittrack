from django.db import models

from .matricula import Matricula

class Plano(models.Model):
    nome = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    duracao = models.PositiveIntegerField(
        help_text="Duração em dias"
    )
    beneficios = models.TextField()

    def __str__(self):
        return self.nome

    def calcular_valor(self):
        return self.valor

    def verificar_validade(self):
        return self.matriculas.filter(status=Matricula.Status.ATIVA).exists()