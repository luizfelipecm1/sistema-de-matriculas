from model import Usuario

from util import CAMINHO_USUARIOS, ler_arquivo


def buscarUser(email: str):
    usuarios : dict = ler_arquivo(CAMINHO_USUARIOS)
    usuario = usuarios.get(email, None)
    if usuario == None:
        print("Usuario não encontrado")
        return None
    usuario = Usuario.model_validate(usuario)
    return usuario

        


    

    





