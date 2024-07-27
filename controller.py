import json
from model import Arch

class Controller:
    def __init__(self, view):
        self.view = view
        self.arch = Arch()
        self.view.set_controller(self)

    def controlador(self, user_info):
        user_info_json = json.dumps(user_info, indent=4)
        mensaje = self.arch.crear_arch(user_info_json)
        print(mensaje)
