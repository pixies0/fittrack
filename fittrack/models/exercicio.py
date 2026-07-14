from django.db import models

class Exercicio(models.Model):
    treino = models.ForeignKey(
        "Treino",
        on_delete=models.CASCADE,
        related_name="exercicios"
    )

    nome = models.CharField(max_length=100)
    series = models.PositiveIntegerField()
    repeticoes = models.PositiveIntegerField()
    carga = models.DecimalField(max_digits=6, decimal_places=2)
    descanso = models.PositiveIntegerField(
        help_text="Descanso em segundos"
    )

    def __str__(self):
        return self.nome

    def calcular_volume(self):
        return self.series * self.repeticoes * self.carga

    def alterar_carga(self, nova_carga):
        self.carga = nova_carga
        self.save()