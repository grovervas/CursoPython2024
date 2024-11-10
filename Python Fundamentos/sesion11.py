#Programación Orientada a Objetos

class Persona:
    def __init__(self, nom, ape, ed):
        self.nombre = nom
        self.apellido = ape
        self.edad = ed
    
    def saludar(self):
        print("Hola, yo me llamo", self.nombre, self.apellido, " y tengo ", self.edad, "años")

class Cliente(Persona):
    def saludarS(self):
        print("Hola")
        
class Empleado(Persona):
    def saludarE(self):
        print("Hola soy un empleado y me llamo", self.nombre)

usuario = Persona('Pablo', 'Lopez', 35)
cliente = Cliente('Ana', 'Perez', 30)
empleado = Empleado('Carlos', 'Vasquez', 25)
empleado.saludarE()


