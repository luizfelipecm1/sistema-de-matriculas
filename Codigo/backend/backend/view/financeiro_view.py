from model import matricula
from controller.financeiro_controller import cobrarMatricula

def view_cobrar_matricula():
    print("-------------Financeiro----------------")

    matricula.idMatricula = input("Digite o id de matricula do aluno para cobrar matricula")

    cobrarMatricula(matricula.idMatricula)

    print("Cobrança finalizada")


