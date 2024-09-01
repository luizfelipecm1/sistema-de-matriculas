from util import menu, divider
from controller import financeiro_controller
from model import financeiro, usuario
from model.aluno import Aluno
from view import login_view
from model.usuario import Tipo
from datetime import datetime


def menu_financeiro():
    menu(
        header="Menu Financeiro",
        opcoes={"Cobrar Matricula ": cobrar_matricula},
        voltar=login_view.menu_login
    )


def cobrar_matricula():
    divider()
    print("Cobrança de Matrícula")
    # idAluno = email
    while True:
        email = input(
            "Insira o email do aluno que sera feita a cobrança \n Email: ")
        usuario = financeiro_controller.buscarUser(email=email)
        if usuario.tipo == Tipo.Aluno:
            print("====Aluno encontrado!====")
            break
        else:
            print("==Esse email não corresponde a um aluno!==")

    try:

        financeiro.valor = float(input("Valor: "))
        data_input = input("Data de cobrança (dd-mm-yyyy): ")

        try:
            financeiro.data = datetime.strptime(data_input, '%d-%m-%Y').strftime('%d-%m-%Y')
        except ValueError:
            print("Formato de data inválido. Use o formato dd-mm-yyyy.")
            return
    
        
        print("Cobrança registrada com sucesso.") 
    except ValueError:
        print("Valor informado não é válido. ")
    except Exception as e:
        print(f"Erro inesperado: {e}")

    finally:
        divider()
        print(f"Processo de cobrança finalizado")
        divider()
        print(f"Aluno: {usuario.nome}")
        print(f"Email Aluno: {usuario.email}")
        print(f"Valor: R${financeiro.valor}")
        print(f"Data: {financeiro.data}")
