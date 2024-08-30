import json
from model import Professor
from util import CAMINHO_USUARIOS


def cadastrar_professor(nome: str, email: str, senha: str, cpf: str):
    professor = Professor(nome=nome, tipo="professor", email=email, senha=senha, cpf=cpf)

    with open(CAMINHO_USUARIOS) as f:
        data = json.load(f)

    data.append(professor.model_dump())

    with open(CAMINHO_USUARIOS, "w") as f:
        json.dump(data, f, indent=4)
