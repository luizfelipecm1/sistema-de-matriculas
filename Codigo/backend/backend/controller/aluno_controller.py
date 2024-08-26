import json
from model import Aluno


def cadastrar_aluno(nome: str, email: str, senha: str, cpf: str):
    aluno = Aluno(nome=nome, tipo="aluno", email=email, senha=senha, cpf=cpf)

    with open("database/usuarios.json") as f:
        data = json.load(f)

    data.append(aluno.model_dump())

    with open("database/usuarios.json", "w") as f:
        json.dump(data, f, indent=4)
