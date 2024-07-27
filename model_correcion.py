import json

class Arch:
    def __init__(self):
        self.datos = None

    def get_datos(self):
        return self.datos
    
    def set_datos(self, auxdatos):
        self.datos = auxdatos

    def crear_arch(self, datos_json):
        name_arch = "Form_dateBase"
        nombre_arch = name_arch + ".txt"
        with open(nombre_arch, "w") as archivo_text:
            archivo_text.write(datos_json)
            mensaje = "document created"
        return mensaje
    
    def read_arch(self):
        nombre_arch = "Form_dateBase.txt"
        with open(nombre_arch, "r") as archive:
            date_content = archive.read()
            print(date_content)
