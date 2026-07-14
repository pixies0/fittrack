from django.urls import path

from .views import (
    DashboardView,
    AlunoCreateView,
    AlunoListView,
    AlunoDetailView,
    AlunoUpdateView,
    AlunoDeleteView,
    ProfessorCreateView,
    ProfessorListView,
    ProfessorDetailView,
    ProfessorUpdateView,
    ProfessorDeleteView,
    PlanoCreateView,
    PlanoListView,
    PlanoDetailView,
    PlanoUpdateView,
    PlanoDeleteView,
    MatriculaCreateView,
    MatriculaListView,
    MatriculaDetailView,
    MatriculaUpdateView,
    MatriculaDeleteView,
    TreinoCreateView,
    TreinoListView,
    TreinoUpdateView,
    TreinoDetailView,
    TreinoDeleteView,
    ExercicioCreateView,
    ExercicioListView,
    ExercicioDetailView,
    ExercicioUpdateView,
    ExercicioDeleteView,
    AvaliacaoFisicaCreateView,
    AvaliacaoFisicaListView,
    AvaliacaoFisicaDetailView,
    AvaliacaoFisicaUpdateView,
    AvaliacaoFisicaDeleteView,
    HistoricoDetailView,
    PerfilView,
    ConfiguracoesView,
)

urlpatterns = [
    path("", DashboardView.as_view(), name="dashboard"),
    # ALUNO
    path("aluno/", AlunoListView.as_view(), name="aluno-list"),
    path("aluno/novo/", AlunoCreateView.as_view(), name="aluno-create"),
    path("aluno/<int:pk>/", AlunoDetailView.as_view(), name="aluno-detail"),
    path("aluno/<int:pk>/editar/", AlunoUpdateView.as_view(), name="aluno-update"),
    path("aluno/<int:pk>/excluir/", AlunoDeleteView.as_view(), name="aluno-delete"),
    # PROFESSOR
    path("professor/", ProfessorListView.as_view(), name="professor-list"),
    path("professor/novo/", ProfessorCreateView.as_view(), name="professor-create"),
    path("professor/<int:pk>/", ProfessorDetailView.as_view(), name="professor-detail"),
    path(
        "professor/<int:pk>/editar/",
        ProfessorUpdateView.as_view(),
        name="professor-update",
    ),
    path(
        "professor/<int:pk>/excluir/",
        ProfessorDeleteView.as_view(),
        name="professor-delete",
    ),
    # PLANO
    path("plano/", PlanoListView.as_view(), name="plano-list"),
    path("plano/novo/", PlanoCreateView.as_view(), name="plano-create"),
    path("plano/<int:pk>/", PlanoDetailView.as_view(), name="plano-detail"),
    path("plano/<int:pk>/editar/", PlanoUpdateView.as_view(), name="plano-update"),
    path("plano/<int:pk>/excluir/", PlanoDeleteView.as_view(), name="plano-delete"),
    # MATRICULA
    path("matricula/", MatriculaListView.as_view(), name="matricula-list"),
    path("matricula/novo/", MatriculaCreateView.as_view(), name="matricula-create"),
    path("matricula/<int:pk>/", MatriculaDetailView.as_view(), name="matricula-detail"),
    path(
        "matricula/<int:pk>/editar/",
        MatriculaUpdateView.as_view(),
        name="matricula-update",
    ),
    path(
        "matricula/<int:pk>/excluir/",
        MatriculaDeleteView.as_view(),
        name="matricula-delete",
    ),
    # TREINO
    path("treino/", TreinoListView.as_view(), name="treino-list"),
    path("treino/novo/", TreinoCreateView.as_view(), name="treino-create"),
    path("treino/<int:pk>/", TreinoDetailView.as_view(), name="treino-detail"),
    path("treino/<int:pk>/editar/", TreinoUpdateView.as_view(), name="treino-update"),
    path("treino/<int:pk>/excluir/", TreinoDeleteView.as_view(), name="treino-delete"),
    # EXERCÍCIO
    path("exercicio/", ExercicioListView.as_view(), name="exercicio-list"),
    path("exercicio/novo/", ExercicioCreateView.as_view(), name="exercicio-create"),
    path("exercicio/<int:pk>/", ExercicioDetailView.as_view(), name="exercicio-detail"),
    path(
        "exercicio/<int:pk>/editar/",
        ExercicioUpdateView.as_view(),
        name="exercicio-update",
    ),
    path(
        "exercicio/<int:pk>/excluir/",
        ExercicioDeleteView.as_view(),
        name="exercicio-delete",
    ),
    # AVALIAÇÃO FÍSICA
    path("avaliacao/", AvaliacaoFisicaListView.as_view(), name="avaliacao-list"),
    path(
        "avaliacao/novo/", AvaliacaoFisicaCreateView.as_view(), name="avaliacao-create"
    ),
    path(
        "avaliacao/<int:pk>/",
        AvaliacaoFisicaDetailView.as_view(),
        name="avaliacao-detail",
    ),
    path(
        "avaliacao/<int:pk>/editar/",
        AvaliacaoFisicaUpdateView.as_view(),
        name="avaliacao-update",
    ),
    path(
        "avaliacao/<int:pk>/excluir/",
        AvaliacaoFisicaDeleteView.as_view(),
        name="avaliacao-delete",
    ),
    # HISTÓRICO
    path("historico/<int:pk>/", HistoricoDetailView.as_view(), name="historico-detail"),
    # PERFIL
    path("perfil/", PerfilView.as_view(), name="perfil"),
    # CONFIGURAÇÕES
    path("configuracoes/", ConfiguracoesView.as_view(), name="configuracoes"),
]
