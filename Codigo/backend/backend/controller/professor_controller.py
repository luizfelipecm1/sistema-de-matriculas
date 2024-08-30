import json
from model import Professor, Disciplina
from view import login_view

from util import CAMINHO_USUARIOS, CAMINHO_DISCIPLINAS, ler_arquivo


def cadastrar_professor(nome: str, email: str, senha: str, cpf: str):
    professor = Professor(nome=nome, tipo="professor", email=email, senha=senha, cpf=cpf)

    with open(CAMINHO_USUARIOS) as f:
        data = json.load(f)

    data.append(professor.model_dump())

    with open(CAMINHO_USUARIOS, "w") as f:
        json.dump(data, f, indent=4)

def listarAlunos(disciplina: Disciplina, disciplina_selecionada: str):
    disciplinas: dict = ler_arquivo(caminho=CAMINHO_DISCIPLINAS)
    dataLogin = login_view.logged_in_user.model_dump_json()
    validaLogin = json.loads(dataLogin)
    while True:
        for _, disciplina in disciplinas.items():
            if disciplina["nome"] == disciplina_selecionada and validaLogin["email"] == disciplina["professor"]["email"]:
                print(f"Disciplina: {disciplina["nome"]}, Ativa: {disciplina["ativa"]}")
                print("Alunos:")
                for aluno in disciplina["alunos"]:
                    print(f"Nome: {aluno['nome']}, Email: {aluno['email']}, CPF: {aluno['cpf']}")
                print("Usuários listados com sucesso!")
                return
            else:
                disciplina_selecionada = input("Essa disciplina não está cadastrada para você. Por favor, insira o nome da disciplina novamente: ")