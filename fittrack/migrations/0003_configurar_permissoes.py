from django.db import migrations


def configurar_permissoes(apps, schema_editor):

    Group = apps.get_model("auth", "Group")
    Permission = apps.get_model("auth", "Permission")

    administrador = Group.objects.get(name="Administrador")
    professor = Group.objects.get(name="Professor")
    aluno = Group.objects.get(name="Aluno")

    # ==========================
    # Administrador
    # ==========================

    administrador.permissions.set(Permission.objects.all())

    # ==========================
    # Professor
    # ==========================

    permissoes_professor = [
        # Aluno
        "view_aluno",
        # Treino
        "view_treino",
        "add_treino",
        "change_treino",
        "delete_treino",
        # Exercício
        "view_exercicio",
        "add_exercicio",
        "change_exercicio",
        "delete_exercicio",
        # Avaliação Física
        "view_avaliacaofisica",
        "add_avaliacaofisica",
        "change_avaliacaofisica",
        "delete_avaliacaofisica",
        # Matrícula
        "view_matricula",
    ]

    professor.permissions.set(
        Permission.objects.filter(codename__in=permissoes_professor)
    )

    # ==========================
    # Aluno
    # ==========================

    permissoes_aluno = [
        "view_treino",
        "view_avaliacaofisica",
        "view_matricula",
    ]

    aluno.permissions.set(Permission.objects.filter(codename__in=permissoes_aluno))


def remover_permissoes(apps, schema_editor):

    Group = apps.get_model("auth", "Group")

    for nome in [
        "Administrador",
        "Professor",
        "Aluno",
    ]:
        grupo = Group.objects.get(name=nome)

        grupo.permissions.clear()


class Migration(migrations.Migration):
    dependencies = [
        ("fittrack", "0002_criar_grupos"),
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.RunPython(
            configurar_permissoes,
            remover_permissoes,
        ),
    ]
