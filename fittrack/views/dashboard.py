from django.views.generic import TemplateView

from fittrack.mixins.permissions import UsuarioSistemaRequiredMixin


class DashboardView(UsuarioSistemaRequiredMixin, TemplateView):
    template_name = "dashboard/dashboard.html"
