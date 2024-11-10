# Sentencia While
"""
numero = 1
suma_pares = 0
suma_impares = 0

while numero <= 20:
    if numero % 2 == 0:
        suma_pares += numero 
    else:
        suma_impares += numero                 
    
    numero += 1
   
print("La suma de los números pares hasta el 20 es:", suma_pares)
print("La suma de los números impares hasta el 20 es:", suma_impares)
"""

# Sentencia For
# range(stop)
# range(start, stop)
# range(start, stop, step)

suma_pares = 0
suma_impares = 0

for numero in range(0, 21): 
    if numero % 2 == 0:
        suma_pares += numero 
    else:
        suma_impares += numero

print("La suma de los números pares hasta el 20 es:", suma_pares)
print("La suma de los números impares hasta el 20 es:", suma_impares)

edad = 38
miListaEdades = [20, 15, 38, 40, 18]

for valor in miListaEdades:
    print(valor)