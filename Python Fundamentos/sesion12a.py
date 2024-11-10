"""
Simular Gestión de Biblioteca
Descripción
Crear una aplicación de consola simple para gestionar una biblioteca. 
Este permitirá agregar libros, buscar libros por título y autor, 
y mostrar todos los libros disponibles.

Requisitos
Clase Libro
Atributos: 
    titulo (str),  autor (str), anio_publicacion (int), isbn (str)
Métodos:
  _init_(self, titulo, autor, anio_publicacion, isbn): Constructor para inicializar los atributos.
  _str_(self): Método para devolver una representación en cadena del libro.

Clase Biblioteca
Atributos:
 libros (list): Lista para almacenar los libros.
Métodos:
 _init_(self): Constructor que inicializa la lista de libros vacía.
 agregar_libro(self, libro): Método para agregar un libro a la biblioteca.
 buscar_por_titulo(self, titulo): Método para buscar libros por título.
 buscar_por_autor(self, autor): Método para buscar libros por autor.
 mostrar_libros(self): Método para mostrar todos los libros en la biblioteca.

Agregar un menu de opciones
"""
class Libro:
    def __init__(self, titulo, autor, anio_publicacion, isbn):
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion
        self.isbn = isbn
    
    def __str__(self):
        return f'{self.titulo} por {self.autor} ({self.anio_publicacion}) - ISBN:{self.isbn})'

class Biblioteca:
    
    def __init__(self):
        self.libros = []
    
    def agregar_libro(self, libro):
        self.libros.append(libro)
    
    def buscar_por_titulo(self, titulo):
        return [libro for libro in self.libros if titulo.lower() in libro.titulo.lower()]
    
    def buscar_por_autor(self, autor):
        return [libro for libro in self.libros if autor.lower() in libro.autor.lower()]
    
    def mostrar_libros(self):
        for libro in self.libros:
            print(libro)

##### Menu de Opciones #####
def mostrar_menu(opciones):
    print('Seleccionar opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]} ')

def leer_opcion(opciones):
    while(a := input('Opcion:')) not in opciones:
        print('Opción incorrecta, ingrese nuevamente.')
    return a

def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()

def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()   
    
def menu_principal():
    opciones = {
        '1': ('Agregar libro', agregar_libro),
        '2': ('Buscar por titulo', buscar_libro_titulo),
        '3': ('Buscar por autor', buscar_libro_autor),
        '4': ('Mostrar libros', mostrar_libros),
        '5': ('Salir', salir)
    }
    generar_menu(opciones, '5')

def agregar_libro():
    titulo = input('Ingrese titulo:')
    autor = input('Ingrese autor:')
    anio = input('Ingrese el año:')
    isbn = input('Ingrese el ISBN:')
    libro = Libro(titulo, autor, anio, isbn)
    biblioteca.agregar_libro(libro)
    print('Libros agregado')

def buscar_libro_titulo():
    titulo = input('\nIngrese título a buscar:')
    for libro in biblioteca.buscar_por_titulo(titulo):
        print(libro)
    
def buscar_libro_autor():
    autor = input('\nIngrese autor a buscar:')
    for libro in biblioteca.buscar_por_autor(autor):
        print(libro)

def mostrar_libros():
    print('Libros de la Biblioteca')
    biblioteca.mostrar_libros()

def salir():
    print('Saliendo...')

if __name__ == '__main__':
    biblioteca = Biblioteca()
    menu_principal()  

"""
libro1 = Libro('Cien años de Soledad', 'Gabriel García Marquez', 1970, '97811345')
libro2 = Libro('Don Quijote de la Mancha', 'Miguel Cervantes', 1604, '97811489')

biblioteca = Biblioteca()
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

biblioteca.mostrar_libros()

#titulo = input('Ingrese libro a buscar:')
#for libro in biblioteca.buscar_por_titulo(titulo):
#    print(libro)

autor = input('Ingrese el autor:')
for libro in biblioteca.buscar_por_autor(autor):
    print(libro)
"""
    
    