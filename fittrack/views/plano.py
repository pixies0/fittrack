from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)

from fittrack.models import Plano


class PlanoListView(ListView):
    model = Plano
    template_name = "plano/list.html"
    context_object_name = "planos"


class PlanoCreateView(CreateView):
    model = Plano
    template_name = "plano/form.html"


class PlanoDetailView(DetailView):
    model = Plano
    template_name = "plano/detail.html"
    context_object_name = "plano"


class PlanoUpdateView(UpdateView):
    model = Plano
    template_name = "plano/form.html"


class PlanoDeleteView(DeleteView):
    model = Plano
    template_name = "plano/delete.html"
