from model import Usuario
from util import CAMINHO_USUARIOS, ler_arquivo


def login(email: str, senha: str):
    usuarios: dict = ler_arquivo(CAMINHO_USUARIOS)
    usuario = usuarios.get(email, None)

    if usuario != None:
        usuario = Usuario.model_validate(usuario)

        if usuario.senha == senha:
            return usuario
        else:
            print("Senha incorreta.")
            return False
    else:
        print("Usuário não encontrado.")
        return None
