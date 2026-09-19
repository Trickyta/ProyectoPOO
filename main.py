class Persona:
    def __init__(self, nombre, edad, profesion):
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion

    def mostrar_datos(self):
        print(f"Nombre de la persona: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Profesión: {self.profesion}")

    def saludar(self):
        print(f"Hola, soy {self.nombre}")

    def mostrar_rol(self):
        print(f"{self.nombre} participa como estudiante en el proyecto.")


persona = Persona("Ricardo", 22, "Estudiante")
persona.mostrar_datos()
persona.saludar()
persona.mostrar_rol()