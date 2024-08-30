from model import financeiro, matricula 
from model.financeiro import cobrarMatricula
from util import CAMINHO_USUARIOS, escrever_no_arquivo

def cobrarMatricula():
    AlunoMatricula = matricula.idMatricula
    if not AlunoMatricula:
        print("Não foi encontrado nenhum aluno com esse numero de matrícula")
        return 
    
    if AlunoMatricula.paga:
        print("Matricula ja foi paga")
        return
    
    financeiro.cobrarMatricula(AlunoMatricula)

    escrever_no_arquivo(AlunoMatricula, CAMINHO_USUARIOS)

    print("A matricula do aluno foi cobrada com sucesso")



    

    





