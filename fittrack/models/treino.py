from django.db import models


class Treino(models.Model):
    matricula = models.ForeignKey(
        "Matricula", on_delete=models.CASCADE, related_name="treinos"
    )

    professor = models.ForeignKey(
        "Professor", on_delete=models.SET_NULL, null=True, related_name="treinos"
    )

    nome = models.CharField(max_length=100)
    objetivo = models.TextField()
    observacoes = models.TextField(blank=True)

    def __str__(self):
        return self.nome

    def adicionar_exercicio(self):
        pass

    def remover_exercicio(self):
        pass
