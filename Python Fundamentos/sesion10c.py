def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_a_celsius(fah):
    return (fah - 32) * 5/9

def conversor():
    print("Seleccionar una conversion")
    print("1. Celsius a Fahrenheit")
    print("2. Fahrenheit a Celsius")
    
    opcion = input("Ingrese la opción (1/2): ")
    
    if opcion == '1':
        celsius = float(input("Ingrese la temperatura celsius: "))
        print(f"Resultado: {celsius_a_fahrenheit(celsius)} Fahrenheit")
    elif opcion == '2':
        fah = float(input("Ingrese la temperatura fahrenheit: "))
        print(f"Resultado: {fahrenheit_a_celsius(fah)} Celsius")
    else:
        print("Opcion incorrecta")

conversor()
    