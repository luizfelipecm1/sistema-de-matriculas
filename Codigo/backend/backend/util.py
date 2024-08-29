import json

CAMINHO_CURSOS = "database/cursos.json"
CAMINHO_DISCIPLINAS = "database/disciplinas.json"
CAMINHO_USUARIOS = "database/usuarios.json"


def divider():
    print("==========================")


def menu(opcoes: dict, header: str = None, voltar=None):
    """
    Menu genérico para printar no terminal as funções que o usuário pode desempenhar.
    Utilizado para navegação do sistema.

    Argumentos:
    header -- texto aparente no topo do menu
    opcoes -- opcoes de seleção do usuário
    voltar -- função de retorno do usuário (ao apertar 9)
    """
    # Print dos itens do menu
    divider()
    if header:
        print(header)
        print()
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


def ler_arquivo(caminho: str):
    with open(caminho) as f:
        dados = json.load(f)

    return dados


def escrever_no_arquivo(caminho: str, dados: dict):
    with open(caminho, "w") as f:
        json.dump(dados, f, indent=4)


def pedir_dados_usuario():
    nome = input("Nome: ")
    email = input("Email: ")
    senha = input("Senha: ")
    cpf = input("Cpf: ")

    return nome, email, senha, cpf
