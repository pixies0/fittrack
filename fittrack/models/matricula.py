from django.db import models

class Matricula(models.Model):

    class Status(models.TextChoices):
        ATIVA = "ATIVA", "Ativa"
        VENCIDA = "VENCIDA", "Vencida"
        CANCELADA = "CANCELADA", "Cancelada"

    aluno = models.ForeignKey(
        "Aluno",
        on_delete=models.CASCADE,
        related_name="matriculas"
    )

    plano = models.ForeignKey(
        "Plano",
        on_delete=models.PROTECT,
        related_name="matriculas"
    )

    data_inicio = models.DateField()
    data_fim = models.DateField()
    status = models.CharField(
        max_length=15,
        choices=Status.choices,
        default=Status.ATIVA
    )

    def __str__(self):
        return f"{self.aluno} - {self.plano}"

    def matricula_ativa(self):
        return self.status == self.Status.ATIVA

    def renovar_plano(self):
        pass