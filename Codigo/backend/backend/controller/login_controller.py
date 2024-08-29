from model import Usuario
from util import CAMINHO_USUARIOS, ler_arquivo


def login(email: str, senha: str):
    usuarios: dict = ler_arquivo(CAMINHO_USUARIOS)
    usuario = usuarios.get(email, None)

    if usuario == None:
        print("Usuário não encontrado.")
        return None

    usuario = Usuario.model_validate(usuario)

    if usuario.senha != senha:
        print("Senha incorreta.")
        return False

    return usuario
