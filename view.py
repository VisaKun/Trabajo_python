import tkinter as tk

class ViewTxt:
    def __init__(self, controller):
        
        self.root = tk.Tk()
        self.root.title("Trabajo Python")
        self.root.geometry("600x400")
        self.root.configure(background="white")
        
        self.container= tk.Frame(self.root, bg= "gray", width= 600, height= 400)
        self.container.pack(fill="both", expand=True)
        
        self.Label1= self.label_create(self.container, "Ingrese su nombre completo:", 0)
        self.label2= self.label_create(self.container, "Ingrese su correo electronico", 1)
        
        #RADIOBUTTONS
        self.document_type= tk.StringVar()
        self.document_type.set("Cedula de ciudadania") 
        
        self.document_type_CC= tk.Radiobutton(self.container, text= "Cedula de ciudadania", variable= self.document_type, value= "Cedula de ciudadania")
        self.document_type_CC.grid(row= 1, column= 1, padx= 5, pady= 10)
        
        self.document_type_TI= tk.Radiobutton(self.container, text= "Tarjeta de identidad", variable= self.document_type, value= "Tarjeta de identidad")
        self.document_type_TI.grid(row= 1, column= 2, padx= 5, pady= 10)
        
        self.document_type_CE= tk.Radiobutton(self.container, text= "Cedula extranjera", variable= self.document_type, value= "Cedula extranjera")
        self.document_type_CE.grid(row= 1, column= 3, padx= 5, pady= 10)
        
        self.document_type_PASSPORT= tk.Radiobutton(self.container, text= "Pasaporte", variable= self.document_type, value= "Pasaporte")
        self.document_type_PASSPORT.grid(row= 1, column= 4, padx= 5, pady= 10)
        
        self.buttonsubmit= tk.Button(self.container, text= "Confirmar informacion", command= self.call_controller)
        self.buttonsubmit.grid(row= 2, column= 2, padx= 10, pady= 10)
        
        self.controller= controller
        
    #MOLDES DE REUTILIZACION DE CODIGO [IGNORE]
    def label_create(self, container, text_label, row_info):
        self.label_create= tk.Label(container, text= text_label)
        self.label_create.grid(row= row_info, column= 0, padx= 5, pady= 10)
        self.entry_create = tk.Entry(container)
        self.entry_create.grid(row= row_info, column= 1, padx= 10, pady= 10)
        return self.entry_create

    #----------------------------------------------------------------#
    
    #FUNCION PARA OBTENER EL TIPO DE DOCUMENTO
    def get_document_type(self):
        return self.document_type.get()
    
    #FUNCION PARA OBTENER LA INFORMACION DEL USUARIO
    def get_user_info(self):
        name = self.Label1.get()
        email = self.Label2.get()
        document_type = self.get_document_type()
        return {
            "name": name,
            "email": email,
            "document_type": document_type
        }
    
    #RECOLECCION DE INFORMACION PARA EL CONTROLADOR    
    def call_controller(self):
        if self.controller is not None:
            user_info = self.get_user_info()
            self.controller.controlador(user_info)