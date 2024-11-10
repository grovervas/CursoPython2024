class Animal:
    def __init__(self, nombre, sonido):
        self.nombre = nombre
        self.sonido = sonido
    
    def saludar(self):
        print("Hola, soy", self.tipo, "y me llamo", self.nombre, "y mi sonido es ", self.sonido)

class Perro(Animal):
    tipo = 'perro'

class Gato(Animal):
    tipo = 'gato'

perro = Perro('Fido', 'Ladrar')
gato = Gato('Silvestre', 'Maullar')

perro.saludar()
gato.saludar()