from django.db import models

class AvaliacaoFisica(models.Model):
    aluno = models.ForeignKey(
        "Aluno",
        on_delete=models.CASCADE,
        related_name="avaliacoes"
    )

    data = models.DateField()
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    altura = models.DecimalField(max_digits=4, decimal_places=2)
    percentual_gordura = models.DecimalField(max_digits=5, decimal_places=2)
    massa_muscular = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.aluno} - {self.data}"

    def calcular_imc(self):
        return float(self.peso) / (float(self.altura) ** 2)

    def gerar_relatorio(self):
        pass