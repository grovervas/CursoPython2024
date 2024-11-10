#Manejo de Excepciones (Control de los errores)
#Try-Except
#Try: Bloque código que podría lanzar una excepción
#Except: Bloque código que se ejecuta cuando ocurre la excepción
#else: Opcional, se ejecuta si el código en try no alcanza ninguna Exception

while True:
    try:
        edad = int(input('¿Cuál es tu edad? '))
        10/edad
        print(edad)
    except ValueError:
        print('Por favor ingrese un número')
    except ZeroDivisionError:
        print('Ingrese un número distinto a cero')
    else:
        print('Gracias')
        break
    finally:
        print('Código del finally')

"""
def suma(num1, num2):
    try:
        return num1/num2
    except (TypeError, ZeroDivisionError) as err:
        print(f'Error: {err}')

print(suma(1, '0'))
"""