from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)

from fittrack.models import Treino


class TreinoListView(ListView):
    model = Treino
    template_name = "treino/list.html"
    context_object_name = "treinos"


class TreinoCreateView(CreateView):
    model = Treino
    template_name = "treino/form.html"


class TreinoDetailView(DetailView):
    model = Treino
    template_name = "treino/detail.html"
    context_object_name = "treino"


class TreinoUpdateView(UpdateView):
    model = Treino
    template_name = "treino/form.html"


class TreinoDeleteView(DeleteView):
    model = Treino
    template_name = "treino/delete.html"
