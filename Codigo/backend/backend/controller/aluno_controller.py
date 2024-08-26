import json
from model import Aluno
from util import CAMINHO_USUARIOS


def cadastrar_aluno(nome: str, email: str, senha: str, cpf: str):
    aluno = Aluno(nome=nome, tipo="aluno", email=email, senha=senha, cpf=cpf)

    with open(CAMINHO_USUARIOS) as f:
        data = json.load(f)

    data.append(aluno.model_dump())

    with open(CAMINHO_USUARIOS, "w") as f:
        json.dump(data, f, indent=4)
