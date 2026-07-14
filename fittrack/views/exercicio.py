from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)

from fittrack.models import Exercicio


class ExercicioListView(ListView):
    model = Exercicio
    template_name = "exercicio/list.html"


class ExercicioCreateView(CreateView):
    model = Exercicio
    template_name = "exercicio/form.html"


class ExercicioDetailView(DetailView):
    model = Exercicio
    template_name = "exercicio/detail.html"


class ExercicioUpdateView(UpdateView):
    model = Exercicio
    template_name = "exercicio/form.html"


class ExercicioDeleteView(DeleteView):
    model = Exercicio
    template_name = "exercicio/delete.html"
