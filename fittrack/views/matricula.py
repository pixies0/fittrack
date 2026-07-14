from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)

from fittrack.models import Matricula


class MatriculaListView(ListView):
    model = Matricula
    template_name = "matricula/list.html"


class MatriculaCreateView(CreateView):
    model = Matricula
    template_name = "matricula/form.html"


class MatriculaDetailView(DetailView):
    model = Matricula
    template_name = "matricula/detail.html"


class MatriculaUpdateView(UpdateView):
    model = Matricula
    template_name = "matricula/form.html"


class MatriculaDeleteView(DeleteView):
    model = Matricula
    template_name = "matricula/delete.html"
