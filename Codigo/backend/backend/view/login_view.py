from controller import login_controller
from model import Tipo
from util import divider, menu
from view import aluno_view, professor_view, secretario_view


def menu_login():
    menu(opcoes={"Login": login})


def login():
    divider()
    print("Login")
    print()

    email = input("Email: ")
    senha = input("Senha: ")
    usuario = login_controller.login(email=email, senha=senha)

    if usuario != None and usuario != False:
        match usuario.tipo:
            case Tipo.Aluno:
                aluno_view.menu_aluno()
            case Tipo.Professor:
                professor_view.menu_professor()
            case Tipo.Secretario:
                secretario_view.menu_secretario()
    else:
        menu_login()
