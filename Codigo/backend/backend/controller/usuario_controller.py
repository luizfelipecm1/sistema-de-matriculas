import json
from model import Tipo, Usuario
from util import CAMINHO_USUARIOS, escrever_no_arquivo, ler_arquivo


def cadastrar(usuario: Usuario):
    usuarios: dict = ler_arquivo(CAMINHO_USUARIOS)
    usuario_cadastrado = usuarios.get(usuario.email, None)

    if usuario_cadastrado != None:
        print("Email já cadastrado no sistema.")
        return

    usuarios[usuario.email] = usuario.model_dump()

    escrever_no_arquivo(CAMINHO_USUARIOS, usuarios)

    print("Usuário cadastrado com sucesso!")


def listar(tipo: Tipo):
    usuarios: dict = ler_arquivo(CAMINHO_USUARIOS)

    for _, usuario in usuarios.items():
        if usuario["tipo"] == tipo:
            print(f"Nome: {usuario["nome"]}, Email: {usuario["email"]}, CPF: {usuario["cpf"]}")

    print("Usuários listados com sucesso!")


def editar(email_atual: str, usuario: Usuario):
    usuarios: dict = ler_arquivo(CAMINHO_USUARIOS)
    
    if email_atual not in usuarios:
        print("Este email não está cadastrado.")
        return
    
    usuarios[usuario.email] = usuario.model_dump()

    if usuario.email != email_atual:
        del usuarios[email_atual]

    escrever_no_arquivo(CAMINHO_USUARIOS, usuarios)

    print("Usuário editado com sucesso!")


def remover(email: str):
    usuarios: dict = ler_arquivo(CAMINHO_USUARIOS)

    if email not in usuarios:
        print("Este email não está cadastrado.")
        return
    
    del usuarios[email]

    escrever_no_arquivo(CAMINHO_USUARIOS, usuarios)

    print("Usuário removido com sucesso!")
