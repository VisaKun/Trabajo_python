class arch:
    def __init__(self):
        self.datos=None

    def get_datos(self):
        return self.datos
    
    def set_datos(self,auxdatos):
        self.datos=auxdatos

    def crearArch(datotexto):
        nameArch=("Form_dateBase")
        nombrearch=nameArch+".txt"
        with open(nombrearch,"w") as archivoText:
             archivoText.write(datotexto)
             mensaje= "document creat "
        archivoText.close()
        return mensaje
    
    def readArch():
        with open("form_dateBase","r") as archive:
            dateContend=archive.read
            print(dateContend)
            archive.close
