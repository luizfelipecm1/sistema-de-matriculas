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
            "Gerênciar Alunos": partial(print, "gerenciar alunos"),
            "Gerênciar Professores": partial(print, "gerenciar professores"),
        },
        voltar=menu_login,
    )


def menu_login():
    menu(opcoes={"Login": partial(print, "login")})


def run():
    print("**Sistema de Matrículas**")
    menu_login()


if __name__ == "__main__":
    run()
