from view import login_view
from util import menu

def menu_aluno():
    menu(header="Bem vindo, Aluno(a)!", opcoes={}, voltar=login_view.menu_login)