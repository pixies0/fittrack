from .dashboard import DashboardView
from .aluno import (
    AlunoCreateView,
    AlunoListView,
    AlunoDetailView,
    AlunoUpdateView,
    AlunoDeleteView,
)
from .professor import (
    ProfessorCreateView,
    ProfessorListView,
    ProfessorDetailView,
    ProfessorUpdateView,
    ProfessorDeleteView,
)
from .plano import (
    PlanoCreateView,
    PlanoListView,
    PlanoDetailView,
    PlanoUpdateView,
    PlanoDeleteView,
)
from .matricula import (
    MatriculaCreateView,
    MatriculaListView,
    MatriculaDetailView,
    MatriculaUpdateView,
    MatriculaDeleteView,
)
from .treino import (
    TreinoCreateView,
    TreinoListView,
    TreinoUpdateView,
    TreinoDetailView,
    TreinoDeleteView,
)
from .exercicio import (
    ExercicioCreateView,
    ExercicioListView,
    ExercicioDetailView,
    ExercicioUpdateView,
    ExercicioDeleteView,
)
from .avaliacao_fisica import (
    AvaliacaoFisicaCreateView,
    AvaliacaoFisicaListView,
    AvaliacaoFisicaDetailView,
    AvaliacaoFisicaUpdateView,
    AvaliacaoFisicaDeleteView,
)
from .historico import HistoricoDetailView
from .perfil import PerfilView
from .configuracoes import ConfiguracoesView
from .autenticacao import (
    UsuarioLoginView,
    UsuarioLogoutView,
)
from .errors import permission_denied

__all__ = [
    "DashboardView",
    "AlunoCreateView",
    "AlunoListView",
    "AlunoDetailView",
    "AlunoUpdateView",
    "AlunoDeleteView",
    "ProfessorCreateView",
    "ProfessorListView",
    "ProfessorDetailView",
    "ProfessorUpdateView",
    "ProfessorDeleteView",
    "PlanoCreateView",
    "PlanoListView",
    "PlanoDetailView",
    "PlanoUpdateView",
    "PlanoDeleteView",
    "MatriculaCreateView",
    "MatriculaListView",
    "MatriculaDetailView",
    "MatriculaUpdateView",
    "MatriculaDeleteView",
    "TreinoCreateView",
    "TreinoListView",
    "TreinoUpdateView",
    "TreinoDetailView",
    "TreinoDeleteView",
    "ExercicioCreateView",
    "ExercicioListView",
    "ExercicioDetailView",
    "ExercicioUpdateView",
    "ExercicioDeleteView",
    "AvaliacaoFisicaCreateView",
    "AvaliacaoFisicaListView",
    "AvaliacaoFisicaDetailView",
    "AvaliacaoFisicaUpdateView",
    "AvaliacaoFisicaDeleteView",
    "HistoricoDetailView",
    "PerfilView",
    "ConfiguracoesView",
    "UsuarioLoginView",
    "UsuarioLogoutView",
    "permission_denied",
]
