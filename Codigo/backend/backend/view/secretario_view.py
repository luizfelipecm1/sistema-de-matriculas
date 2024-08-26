from controller import usuario_controller
from functools import partial
from model import Usuario, Tipo
from util import divider, menu
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
            "Cadastrar": partial(cadastrar_usuario, tipo=Tipo.Aluno),
            "Editar": partial(print, "editar aluno"),
            "Remover": partial(print, "remover aluno"),
        },
        voltar=menu_secretario,
    )


def cadastrar_usuario(tipo: Tipo):
    divider()
    print(f"Digite os campos do {tipo.value.capitalize()}")

    nome = input("Nome: ")
    email = input("Email: ")
    senha = input("Senha: ")
    cpf = input("Cpf: ")

    usuario = Usuario(nome=nome, tipo=tipo, email=email, senha=senha, cpf=cpf)
    usuario_controller.cadastrar(usuario=usuario)

    match tipo:
        case Tipo.Aluno:
            menu_gerencia_alunos()
        case Tipo.Professor:
            pass
        case Tipo.Secretario:
            pass
