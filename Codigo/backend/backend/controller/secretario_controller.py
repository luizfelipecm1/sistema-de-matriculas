from model import Curso, Disciplina, Tipo, Semestre, Usuario
from util import CAMINHO_CURSOS, CAMINHO_DISCIPLINAS, CAMINHO_USUARIOS, escrever_no_arquivo, ler_arquivo


def gerarCurriculo(curso: Curso, disciplinas: list[Disciplina]):
    cursos: dict = ler_arquivo(CAMINHO_CURSOS)
    
    periodo = curso.semestres[-1].periodo + 1 if curso.semestres else 1

    semestre = Semestre(periodo=periodo, disciplinas=disciplinas)
    curso.semestres.append(semestre)
    cursos[curso.nome] = curso.model_dump()
    
    escrever_no_arquivo(CAMINHO_CURSOS, cursos)

    print("Currículo do semestre gerado com sucesso!")


def cadastrarUsuario(usuario: Usuario):
    usuarios: dict = ler_arquivo(CAMINHO_USUARIOS)
    usuario_cadastrado = usuarios.get(usuario.email, None)

    if usuario_cadastrado != None:
        print("Email já cadastrado no sistema.")
        return

    usuarios[usuario.email] = usuario.model_dump()

    escrever_no_arquivo(CAMINHO_USUARIOS, usuarios)

    print("Usuário cadastrado com sucesso!")


def listarUsuarios(tipo: Tipo):
    usuarios: dict = ler_arquivo(CAMINHO_USUARIOS)

    for _, usuario in usuarios.items():
        if usuario["tipo"] == tipo:
            print(f"Nome: {usuario["nome"]}, Email: {usuario["email"]}, CPF: {usuario["cpf"]}")

    print("Usuários listados com sucesso!")


def editarUsuario(email_atual: str, usuario: Usuario):
    usuarios: dict = ler_arquivo(CAMINHO_USUARIOS)
    
    if email_atual not in usuarios:
        print("Este email não está cadastrado.")
        return
    
    usuarios[usuario.email] = usuario.model_dump()

    if usuario.email != email_atual:
        del usuarios[email_atual]

    escrever_no_arquivo(CAMINHO_USUARIOS, usuarios)

    print("Usuário editado com sucesso!")


def removerUsuario(email: str):
    usuarios: dict = ler_arquivo(CAMINHO_USUARIOS)

    if email not in usuarios:
        print("Este email não está cadastrado.")
        return
    
    del usuarios[email]

    escrever_no_arquivo(CAMINHO_USUARIOS, usuarios)

    print("Usuário removido com sucesso!")


def cadastrarDisciplina(disciplina: Disciplina):
    disciplinas: dict = ler_arquivo(CAMINHO_DISCIPLINAS)

    disciplinas[disciplina.nome] = disciplina.model_dump()

    escrever_no_arquivo(CAMINHO_DISCIPLINAS, disciplinas)

    print("Disciplina cadastrado com sucesso!")


def cadastrarCurso(curso: Curso):
    disciplinas: dict = ler_arquivo(CAMINHO_CURSOS)

    disciplinas[curso.nome] = curso.model_dump()

    escrever_no_arquivo(CAMINHO_CURSOS, disciplinas)

    print("Curso cadastrado com sucesso!")
