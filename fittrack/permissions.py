from fittrack.constants import Grupos


SIDEBAR_PERMISSIONS = {
    "dashboard": [
        Grupos.ADMINISTRADOR,
        Grupos.PROFESSOR,
        Grupos.ALUNO,
    ],
    "alunos": [
        Grupos.ADMINISTRADOR,
        Grupos.PROFESSOR,
    ],
    "professores": [
        Grupos.ADMINISTRADOR,
    ],
    "planos": [
        Grupos.ADMINISTRADOR,
    ],
    "matriculas": [
        Grupos.ADMINISTRADOR,
        Grupos.PROFESSOR,
    ],
    "treinos": [
        Grupos.ADMINISTRADOR,
        Grupos.PROFESSOR,
        Grupos.ALUNO,
    ],
    "exercicios": [
        Grupos.ADMINISTRADOR,
        Grupos.PROFESSOR,
    ],
    "avaliacoes": [
        Grupos.ADMINISTRADOR,
        Grupos.PROFESSOR,
        Grupos.ALUNO,
    ],
    "historico": [
        Grupos.ADMINISTRADOR,
        Grupos.ALUNO,
    ],
    "perfil": [
        Grupos.ADMINISTRADOR,
        Grupos.PROFESSOR,
        Grupos.ALUNO,
    ],
    "configuracoes": [
        Grupos.ADMINISTRADOR,
    ],
}
