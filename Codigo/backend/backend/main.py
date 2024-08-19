from models import Usuario

def run():
    print("Sistema de Matriculas")
    usuario = Usuario(nome="joao", email="joao@gmail.com", senha="123")
    print(usuario)
    


if __name__ == "__main__":
    run()