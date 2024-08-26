import json
from model import Usuario

def cadastrar(usuario: Usuario):
    with open("database/usuarios.json") as f:
        data = json.load(f)

    data.append(usuario.model_dump())

    with open("database/usuarios.json", "w") as f:
        json.dump(data, f, indent=4)

    print("Usuário cadastrado com sucesso!")