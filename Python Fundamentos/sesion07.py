#-----Tuplas-----
#Estructura de Datos
nombre = 'Grover'
edad = 38
email = 'prueba@mail.com'
casado = True
precio = 5.99

#---- Crear Tuplas------
misNombres = ('Grover', 'Pedro', 'Ana', 'Lili', 'Jose', 'Maria', 'Eduardo', 'Ana', [10, 15, 20])
#               0          1      2       3       4       5         6
#              -7         -6     -5       -4     -3      -2        -1

misNumeros = (10, 50, 1500, 8, 755)
misEstados = (True, False, False, True)
misPrecios = (5.99, 9.99, 89.90)
misDatos = ('Grover', 40, 'Lima', 1999.99, True)
print('-------------------------')

misDatos = ('Pablo', 40, 'Ingeniero', 'Masculino', 'mail@prueba.com')

nombre, edad, profesion, sexo, correo = misDatos
print(misNombres)
misNombres[-1][0] = 30
print(misNombres)

#-----slicing------
print(misNombres[::2])

