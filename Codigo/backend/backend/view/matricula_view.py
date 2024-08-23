from util import menu
from controller import matricula_controller

def menu_matricula():
    menu(opcoes={"Matricula": matricula_controller.create_matricula})
