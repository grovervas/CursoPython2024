#Funciones
# Es un algoritmo con "parámetros" para realizar una determinada acción
#---------------------
# Crear una función
def mi_funcion(nombre, edad):
    
    print(f"Hola {nombre}, tu edad es: {edad}")

mi_funcion(nombre="Grover", edad=38)
mi_funcion(edad=39, nombre="Ana")


print("============================")
def mis_animales(Animales):
    for x in Animales:
        print(x)

animales = ["Gato", "Perro", "Canario"]

mis_animales(animales)

print("============================")

def mi_funcion_variable(*args):
    for x in args:
        print(x)

mi_funcion_variable('Grover', 'Pedro', 'Ana')

print("============================")

def sumar(x, y)->int:
    sum = x + y
    return sum

suma = sumar(5, 8)
print(suma)

print("============================")

def mi_funcion_dos():
    pass

def count_down(n):
    print(n)
    if n==0:
        return
    else:
        n = count_down(n-1)

count_down(3)

print("============================")

def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))