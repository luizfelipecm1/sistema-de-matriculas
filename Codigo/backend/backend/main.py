import json
from functools import partial
from models import Aluno
from utils import divider


def menu(opcoes: dict, header: str = None, voltar=None):
    # Print dos itens do menu
    divider()
    if header:
        print(header)
    i: int = 1
    for opcao in opcoes:
        print(f"{i} - {opcao}")
        i += 1
    print()
    if voltar:
        print("9 - Voltar, 0 - Sair")
    else:
        print("0 - Sair")

    opcao = int(input("Selecione um número: "))
    # Opção válida, chamar função atrelada
    if opcao in range(1, len(opcoes) + 1):
        opcoes[list(opcoes)[opcao - 1]]()
    # Voltar
    elif opcao == 9:
        voltar()
    # Sair
    elif opcao == 0:
        exit()
    # Opção inválida, chamar menu novamente
    else:
        menu(opcoes=opcoes, voltar=voltar)


def menu_secretario():
    menu(
        header="Bem vindo, Secretário(a)!",
        opcoes={
            "Gerar Currículo": partial(print, "gerar curriculo"),
            "Gerenciar Alunos": menu_gerencia_alunos,
            "Gerenciar Professores": partial(print, "gerenciar professores"),
        },
        voltar=menu_login,
    )


def menu_gerencia_alunos():
    menu(
        header="Gerência de Alunos",
        opcoes={
            "Listar": partial(print, "listar alunos"),
            "Cadastrar": cadastrar_aluno,
            "Editar": partial(print, "editar aluno"),
            "Remover": partial(print, "remover aluno"),
        },
        voltar=menu_secretario,
    )


def menu_login():
    menu(opcoes={"Login": menu_gerencia_alunos})


def cadastrar_aluno():
    divider()
    print("Digite os campos do Aluno")

    nome = input("Nome: ")
    email = input("Email: ")
    senha = input("Senha: ")
    cpf = input("Cpf: ")

    aluno = Aluno(nome=nome, email=email, senha=senha, cpf=cpf)

    with open("database/usuarios.json") as f:
        data = json.load(f)

    data.append(aluno.model_dump())

    with open("database/usuarios.json", "w") as f:
        json.dump(data, f, indent=4)


def login():
    print("Login")

    nome = input("Nome: ")
    senha = input("Senha: ")

    # with open("database/usuarios.json", "r") as f:
    #     usuarios = json.load(f)
    #     print(usuarios)


def run():
    # open("database/usuarios.json", "x")
    print("**Sistema de Matrículas**")
    menu_login()


if __name__ == "__main__":
    run()
