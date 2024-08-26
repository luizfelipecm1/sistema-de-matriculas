from controller import usuario_controller
from functools import partial
from model import Tipo, Usuario
from util import divider, menu, pedir_dados_usuario
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
            "Listar": partial(listar_usuario, tipo=Tipo.Aluno),
            "Cadastrar": partial(cadastrar_usuario, tipo=Tipo.Aluno),
            "Editar": partial(editar_usuario, tipo=Tipo.Aluno),
            "Remover": partial(remover_usuario, tipo=Tipo.Aluno),
        },
        voltar=menu_secretario,
    )


def listar_usuario(tipo: Tipo):
    divider()
    usuario_controller.listar(tipo=tipo)

    chamar_menu_gerencia_usuario(tipo=tipo)


def cadastrar_usuario(tipo: Tipo):
    divider()
    print(f"Digite os campos do {tipo.value.capitalize()}")

    nome, email, senha, cpf = pedir_dados_usuario()

    usuario = Usuario(nome=nome, tipo=tipo, email=email, senha=senha, cpf=cpf)
    usuario_controller.cadastrar(usuario=usuario)

    chamar_menu_gerencia_usuario(tipo=tipo)


def editar_usuario(tipo: Tipo):
    divider()
    email_atual = input(f"Digite o email atual do {tipo.value} que deseja editar: ")

    print("Agora digite os novos dados")
    nome, email, senha, cpf = pedir_dados_usuario()

    usuario = Usuario(nome=nome, tipo=tipo, email=email, senha=senha, cpf=cpf)
    usuario_controller.editar(email_atual=email_atual, usuario=usuario)

    chamar_menu_gerencia_usuario(tipo=tipo)


def remover_usuario(tipo: Tipo):
    divider()
    email = input(f"Digite o email do {tipo.value} que deseja remover: ")
    usuario_controller.remover(email=email)

    chamar_menu_gerencia_usuario(tipo=tipo)


def chamar_menu_gerencia_usuario(tipo: Tipo):
    match tipo:
        case Tipo.Aluno:
            menu_gerencia_alunos()
        case Tipo.Professor:
            pass
        case Tipo.Secretario:
            pass
