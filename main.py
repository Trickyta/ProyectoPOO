class Persona:
    def __init__(self, nombre, edad, profesion):
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion

    def mostrar_datos(self):

        print(f"Nombre completo: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Profesión: {self.profesion}")

    def saludar(self):
        print(f"Hola, soy {self.nombre}")

    def mostrar_rol(self):
        print(f"{self.nombre} participa como estudiante en el proyecto.")
        
    def mostrar_mensaje_colaborativo(self):
        print("Este mensaje fue agregado por el colaborador.")
        self.mensaje_colaborativo()

    def mensaje_colaborativo(self):
        print("Este mensaje fue agregado por el colaborador.")

persona = Persona("Ricardo", 22, "Estudiante")
persona.mostrar_datos()
persona.saludar()
persona.mostrar_rol()