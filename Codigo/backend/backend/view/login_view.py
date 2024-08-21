from controller import login_controller
from util import menu


def menu_login():
    menu(opcoes={"Login": login_controller.login})
