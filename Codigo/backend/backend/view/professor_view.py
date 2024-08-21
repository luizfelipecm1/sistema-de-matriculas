from util import menu
from view import login_view

def menu_professor():
    menu(header="Bem vindo, Professor(a)!", opcoes={}, voltar=login_view.menu_login)
