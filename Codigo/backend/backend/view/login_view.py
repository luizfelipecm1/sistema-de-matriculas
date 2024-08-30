from controller import login_controller
from model import Tipo
from util import divider, menu
from view import aluno_view, professor_view, secretario_view
logged_in_user = None


def menu_login():
    menu(opcoes={"Login": login})


def login():
    global logged_in_user
    divider()
    print("Login")
    print()

    email = input("Email: ")
    senha = input("Senha: ")
    usuario = login_controller.login(email=email, senha=senha)

    if usuario != None and usuario != False:
        logged_in_user = usuario
        match usuario.tipo:
            case Tipo.Aluno:
                aluno_view.menu_aluno()
            case Tipo.Professor:
                professor_view.menu_professor()
            case Tipo.Secretario:
                secretario_view.menu_secretario()
        return

    menu_login()
