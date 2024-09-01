from util import menu
from controller import matricula_controller
from view import login_view

def menu_matricula():
    menu(
        header="Matrícula!",
        opcoes={
            "Realizar matricula": matricula_controller.create_matricula,
            "Editar matricula": matricula_controller.editar_matricula,
            "Excluir matricula": matricula_controller.excluir_matricula,
        },
        voltar=login_view.menu_login
        )

