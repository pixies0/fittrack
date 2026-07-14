from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)

from fittrack.models import Aluno


class AlunoListView(ListView):
    model = Aluno
    template_name = "aluno/list.html"
    context_object_name = "alunos"


class AlunoCreateView(CreateView):
    model = Aluno
    template_name = "aluno/form.html"


class AlunoDetailView(DetailView):
    model = Aluno
    template_name = "aluno/detail.html"
    context_object_name = "aluno"


class AlunoUpdateView(UpdateView):
    model = Aluno
    template_name = "aluno/form.html"


class AlunoDeleteView(DeleteView):
    model = Aluno
    template_name = "aluno/delete.html"
