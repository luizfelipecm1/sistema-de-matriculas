from models import Aluno
from functools import partial


def menu(opcoes: dict, header: str = None, voltar=None):
    # Print dos itens do menu
    print("==========================")
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
    menu(opcoes={"Login": menu_secretario})


def cadastrar_aluno():
    print("Digite os campos do Aluno")

    nome = input("Nome: ")
    email = input("Email: ")
    senha = input("Senha: ")
    cpf = input("Cpf: ")

    aluno = Aluno(nome=nome, email=email, senha=senha, cpf=cpf)

    f = open("database/usuarios", "a")
    f.write(aluno.model_json_schema())


def run():
    print("**Sistema de Matrículas**")
    menu_login()


if __name__ == "__main__":
    run()
