import json
from model import Usuario, Tipo
from util import divider
from view import aluno_view, login_view, professor_view, secretario_view

def login():
    divider()
    print("Login")
    print()

    email = input("Email: ")
    senha = input("Senha: ")

    with open("database/usuarios.json", "r") as f:
        usuarios = json.load(f)

    usuario = next((usuario for usuario in usuarios if usuario["email"] == email), None)

    if usuario != None:
        usuario = Usuario.model_validate(usuario)

    if usuario == None:
        print("Usuário não encontrado.")
        login_view.menu_login()
    elif usuario.senha == senha:
        match usuario.tipo:
            case Tipo.Aluno:
                aluno_view.menu_aluno()
            case Tipo.Professor:
                professor_view.menu_professor()
            case Tipo.Secretario:
                secretario_view.menu_secretario()
    else:
        print("Senha incorreta.")
        login_view.menu_login()