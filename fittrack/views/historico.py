from django.views.generic import DetailView

from fittrack.models import Aluno


class HistoricoDetailView(DetailView):
    model = Aluno
    template_name = "historico/detail.html"
