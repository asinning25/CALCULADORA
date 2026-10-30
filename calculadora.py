# Calculadora simple usando funciones

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: no se puede dividir entre cero"
    else:
        return a / b

def potencia(a, b):
    return a ** b

# Menú principal
opcion = 1

while opcion != 0:
    print("\n=== CALCULADORA ===")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Potencia")
    print("0. Salir")
    
    opcion = int(input("Elige una opción: "))
    
    if opcion == 0:
        print("Adiós")
    elif opcion >= 1 and opcion <= 5:
        a = float(input("Primer número: "))
        b = float(input("Segundo número: "))
        
        if opcion == 1:
            print("Resultado:", sumar(a, b))
        elif opcion == 2:
            print("Resultado:", restar(a, b))
        elif opcion == 3:
            print("Resultado:", multiplicar(a, b))
        elif opcion == 4:
            print("Resultado:", dividir(a, b))
        elif opcion == 5:
            print("Resultado:", potencia(a, b))
    else:
        print("Opción no válida")