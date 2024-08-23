import json
from model import Usuario


def login(email: str, senha: str):
    with open("database/usuarios.json", "r") as f:
        usuarios = json.load(f)

    usuario = next((usuario for usuario in usuarios if usuario["email"] == email), None)

    if usuario != None:
        usuario = Usuario.model_validate(usuario)

        if usuario.senha == senha:
            return usuario
        else:
            print("Senha incorreta.")
            return False
    else:
        print("Usuário não encontrado.")
        return None
