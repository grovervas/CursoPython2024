#-----Listas-----
#Estructura de Datos
nombre = 'Grover'
edad = 38
email = 'prueba@mail.com'
casado = True
precio = 5.99

#---- Crear Listas------
misNombres = ['Grover', 'Pedro', 'Ana', 'Lili', 'Jose']
#               0          1      2       3       4
#              -5         -4     -3      -2      -1
misNumeros = [10, 50, 1500, 8, 755]
misEstados = [True, False, False, True]
misPrecios = [5.99, 9.99, 89.90]
misDatos = ['Grover', 40, 'Lima', 1999.99, True]
print('-------------------------')
#---Limpiar la lista-----
print(misNumeros)
misNumeros.clear()
print(misNumeros)

#---Remover elementos---
print(misNombres)
misNombres.remove('Pedro')
print(misNombres)
valor = misNombres.pop(-3)
print(misNombres)
print(valor)

#--- Insertar elementos----
#print(misDatos) 
#misDatos.insert(3, 'Bogota')
#misDatos.insert(6, 'Roberto')
#print(misDatos)

"""
#--- Agregar elementos-----
#print(misDatos)
misDatos.append(55)
misDatos.append('Maria')
misDatos.append(False)
#print(misDatos)

#---- Cambiar elementos de la lista ---
print(misNombres[3])
misNombres[3] = 'Luis'
print(misNombres[3])

#---- Leer datos de la lista----
#print(misNombres[3])

#----Tamaño de una lista------
size = len(misEstados)
print(size)

#---- Mostrar Listas------
print(misNombres)
print(misNumeros)
print(misEstados)
print(misPrecios)
print(misDatos)
"""
