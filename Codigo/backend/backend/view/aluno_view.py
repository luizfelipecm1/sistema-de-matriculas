from view import login_view, matricula_view
from util import menu

from model import Curso, Tipo, Usuario
from util import (
    CAMINHO_CURSOS,
    CAMINHO_DISCIPLINAS,
    divider,
    ler_arquivo,
    menu,
    pedir_dados_usuario,
)


def menu_aluno():
    menu(
        header="Bem vindo, Aluno(a)!",
        opcoes={
            "Matrícula": fazer_matricula,
        },
        voltar=login_view.menu_login,
    )


def fazer_matricula():
    matricula_view.menu_matricula()
