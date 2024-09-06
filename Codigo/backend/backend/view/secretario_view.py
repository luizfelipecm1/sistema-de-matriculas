from controller import secretario_controller
from functools import partial
from model import Curso, Disciplina, Professor, Tipo, Usuario
from util import (
    CAMINHO_CURSOS,
    CAMINHO_DISCIPLINAS,
    CAMINHO_USUARIOS,
    divider,
    ler_arquivo,
    menu,
    pedir_dados_usuario,
)
from view import login_view


def menu_secretario():
    menu(
        header="Bem vindo, Secretário(a)!",
        opcoes={
            "Gerenciar Alunos": menu_gerencia_alunos,
            "Gerenciar Professores": menu_gerencia_professores,
            "Gerenciar Cursos/Disciplinas": menu_gerencia_cursos_disciplinas,
        },
        voltar=login_view.menu_login,
    )


def menu_gerencia_cursos_disciplinas():
    menu(
        header="Gerência de Cursos",
        opcoes={
            "Gerar Currículo": gerar_curriculo,
            "Cadastrar Curso": cadastrar_curso,
            "Cadastrar Disciplina": cadastrar_disciplina,
        },
        voltar=menu_secretario,
    )


def gerar_curriculo():
    divider()
    print("Gerar Currículo")
    curso_selecionado = input("Digite o nome do curso que deseja gerar currículo: ")
    cursos: dict = ler_arquivo(caminho=CAMINHO_CURSOS)
    disciplinas: dict = ler_arquivo(caminho=CAMINHO_DISCIPLINAS)

    while curso_selecionado not in cursos:
        print("Curso não encontrado.")
        curso_selecionado = input("Digite o nome do curso que deseja gerar currículo: ")

    curso: Curso = Curso.model_validate(cursos[curso_selecionado])

    print()
    print("Agora preencha os dados do semestre")
    i = 0
    n = int(input("Número de disciplinas: "))

    disciplinas_curriculo = []
    while i < n:
        disciplina = input(f"Disciplina {i+1}: ")

        while disciplina not in disciplinas:
            print("Disciplina não encontrada.")
            disciplina = input(f"Disciplina {i+1}: ")

        disciplinas_curriculo.append(disciplinas[disciplina])
        i += 1

    secretario_controller.gerarCurriculo(curso=curso, disciplinas=disciplinas_curriculo)

    menu_gerencia_cursos_disciplinas()


def cadastrar_curso():
    divider()
    print("Digite os campos da Curso")

    nome = input("Nome: ")
    creditos = input("Créditos: ")

    curso = Curso(nome=nome, creditos=creditos, semestres=[], alunos=[])
    secretario_controller.cadastrarCurso(curso=curso)

    menu_gerencia_cursos_disciplinas()


def cadastrar_disciplina():
    divider()
    print("Digite os campos da Disciplina")

    nome = input("Nome: ")
    email_professor = input("E-mail do professor: ")
    usuarios: dict = ler_arquivo(CAMINHO_USUARIOS)

    while email_professor not in usuarios:
        print("Professor não encontrado.")
        email_professor = input("E-mail do professor: ")

    usuario = usuarios[email_professor]

    while usuario["tipo"] != Tipo.Professor:
        print("Usuário selecionado não é do tipo professor.")
        email_professor = input("E-mail do professor: ")

    professor = Professor.model_validate(usuario)
    disciplina = Disciplina(nome=nome, ativa=False, professor=professor, alunos=[])

    secretario_controller.cadastrarDisciplina(disciplina=disciplina)

    menu_gerencia_cursos_disciplinas()


def menu_gerencia_alunos():
    menu(
        header="Gerência de Alunos",
        opcoes={
            "Listar": partial(listar_usuario, tipo=Tipo.Aluno),
            "Cadastrar": partial(cadastrar_usuario, tipo=Tipo.Aluno),
            "Editar": partial(editar_usuario, tipo=Tipo.Aluno),
            "Remover": partial(remover_usuario, tipo=Tipo.Aluno),
        },
        voltar=menu_secretario,
    )


def menu_gerencia_professores():
    menu(
        header="Gerência de Professores",
        opcoes={
            "Listar": partial(listar_usuario, tipo=Tipo.Professor),
            "Cadastrar": partial(cadastrar_usuario, tipo=Tipo.Professor),
            "Editar": partial(editar_usuario, tipo=Tipo.Professor),
            "Remover": partial(remover_usuario, tipo=Tipo.Professor),
        },
        voltar=menu_secretario,
    )


def listar_usuario(tipo: Tipo):
    divider()
    secretario_controller.listarUsuarios(tipo=tipo)

    chamar_menu_gerencia_usuario(tipo=tipo)


def cadastrar_usuario(tipo: Tipo):
    divider()
    print(f"Digite os campos do {tipo.value.capitalize()}")

    nome, email, senha, cpf = pedir_dados_usuario()

    usuario = Usuario(nome=nome, tipo=tipo, email=email, senha=senha, cpf=cpf)
    secretario_controller.cadastrarUsuario(usuario=usuario)

    chamar_menu_gerencia_usuario(tipo=tipo)


def editar_usuario(tipo: Tipo):
    divider()
    email_atual = input(f"Digite o email atual do {tipo.value} que deseja editar: ")

    print("Agora digite os novos dados")
    nome, email, senha, cpf = pedir_dados_usuario()

    usuario = Usuario(nome=nome, tipo=tipo, email=email, senha=senha, cpf=cpf)
    secretario_controller.editarUsuario(email_atual=email_atual, usuario=usuario)

    chamar_menu_gerencia_usuario(tipo=tipo)


def remover_usuario(tipo: Tipo):
    divider()
    email = input(f"Digite o email do {tipo.value} que deseja remover: ")
    secretario_controller.removerUsuario(email=email)

    chamar_menu_gerencia_usuario(tipo=tipo)


def chamar_menu_gerencia_usuario(tipo: Tipo):
    match tipo:
        case Tipo.Aluno:
            menu_gerencia_alunos()
        case Tipo.Professor:
            menu_gerencia_professores()
        case Tipo.Secretario:
            pass
