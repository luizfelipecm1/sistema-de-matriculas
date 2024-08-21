import json
from model import Aluno
from util import divider


def cadastrar_aluno():
    divider()
    print("Digite os campos do Aluno")

    nome = input("Nome: ")
    email = input("Email: ")
    senha = input("Senha: ")
    cpf = input("Cpf: ")

    aluno = Aluno(nome=nome, tipo="aluno", email=email, senha=senha, cpf=cpf)

    with open("database/usuarios.json") as f:
        data = json.load(f)

    data.append(aluno.model_dump())

    with open("database/usuarios.json", "w") as f:
        json.dump(data, f, indent=4)
