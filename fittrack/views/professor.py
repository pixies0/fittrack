from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)

from fittrack.models import Professor


class ProfessorListView(ListView):
    model = Professor
    template_name = "professor/list.html"
    context_object_name = "professores"


class ProfessorCreateView(CreateView):
    model = Professor
    template_name = "professor/form.html"


class ProfessorDetailView(DetailView):
    model = Professor
    template_name = "professor/detail.html"
    context_object_name = "professor"


class ProfessorUpdateView(UpdateView):
    model = Professor
    template_name = "professor/form.html"


class ProfessorDeleteView(DeleteView):
    model = Professor
    template_name = "professor/delete.html"
