from util import menu
from view import login_view
from model import Disciplina
from controller import professor_controller
from util import (
    CAMINHO_CURSOS,
    CAMINHO_DISCIPLINAS,
    divider,
    ler_arquivo,
    menu,
    pedir_dados_usuario,
)

def menu_professor():
    menu(
        header="Bem vindo, Professor(a)!",
        opcoes={
            "Alunos cadastrados por disciplina": lista_alunos
        },
        voltar=login_view.menu_login,
    )

def lista_alunos():
    divider()
    print("Listar alunos em suas disciplinas")
    disciplina_selecionada = input("Digite o nome da disciplina que você quer ver os alunos cadastrados: ")
    disciplinas: dict = ler_arquivo(caminho=CAMINHO_DISCIPLINAS)
    
    if disciplina_selecionada not in disciplinas:
        print("Disciplina não encontrada.")
        lista_alunos()
        return


    disciplina: Disciplina = Disciplina.model_validate(disciplinas[disciplina_selecionada])
    print()
    professor_controller.listarAlunos(disciplina=disciplina, disciplina_selecionada=disciplina_selecionada)
    
    
    
    