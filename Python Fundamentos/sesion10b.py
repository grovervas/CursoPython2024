def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero"

def calculadora():
    print("Seleccionar una operación:")
    print("===============")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("===============")
    
    opcion = input("Ingrese la opción (1/2/3/4): ")
    
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    
    if opcion == '1':
        print(f"Resultado: {suma(num1, num2)}")
    elif opcion == '2':
        print(f"Resultado: {resta(num1, num2)}")
    elif opcion == '3':
        print(f"Resultado: {multiplicacion(num1, num2)}")
    elif opcion == '4':
        print(f"Resultado: {division(num1, num2)}")
    else:
        print("Opción incorrecta")

calculadora()