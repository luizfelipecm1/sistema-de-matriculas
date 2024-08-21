from controller import aluno_controller
from functools import partial
from util import menu
from view import login_view

def menu_secretario():
    menu(
        header="Bem vindo, Secretário(a)!",
        opcoes={
            "Gerar Currículo": partial(print, "gerar curriculo"),
            "Gerenciar Alunos": menu_gerencia_alunos,
            "Gerenciar Professores": partial(print, "gerenciar professores"),
        },
        voltar=login_view.menu_login,
    )


def menu_gerencia_alunos():
    menu(
        header="Gerência de Alunos",
        opcoes={
            "Listar": partial(print, "listar alunos"),
            "Cadastrar": aluno_controller.cadastrar_aluno,
            "Editar": partial(print, "editar aluno"),
            "Remover": partial(print, "remover aluno"),
        },
        voltar=menu_secretario,
    )
