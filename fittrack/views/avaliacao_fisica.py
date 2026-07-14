from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)

from fittrack.models import AvaliacaoFisica


class AvaliacaoFisicaListView(ListView):
    model = AvaliacaoFisica
    template_name = "avaliacao/list.html"


class AvaliacaoFisicaCreateView(CreateView):
    model = AvaliacaoFisica
    template_name = "avaliacao/form.html"


class AvaliacaoFisicaDetailView(DetailView):
    model = AvaliacaoFisica
    template_name = "avaliacao/detail.html"


class AvaliacaoFisicaUpdateView(UpdateView):
    model = AvaliacaoFisica
    template_name = "avaliacao/form.html"


class AvaliacaoFisicaDeleteView(DeleteView):
    model = AvaliacaoFisica
    template_name = "avaliacao/delete.html"
