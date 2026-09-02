class Persona:
    def __init__(self, nombre, edad, profesion):
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion

    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Profesión: {self.profesion}")

    def saludar(self):
        print(f"Hola, soy {self.nombre}")


persona = Persona("Ricardo", 22, "Estudiante")
persona.mostrar_datos()
persona.saludar()