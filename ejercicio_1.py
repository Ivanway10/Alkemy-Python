#Crear un pequeño programa que realice una función aritmética que permita al usuario ingresar datos por la terminal acorde a distintas opciones.  
#Para ellos debemos definir una función que reciba parámetros:
#Combinar funciones nativas y funciones definidas,
#condicionales, y bucles.
#Si el usuario ingresa el nro 1, realiza la acción A.
#Si el usuario ingresa el nro 2, realiza la acción B.


def accion_a(numero1, numero2):
    resultado = numero1 + numero2
    return resultado

def accion_b(numero1, numero2):
    resultado = numero1 * numero2
    return resultado

def main():
    print("Bienvenido al programa de acciones aritméticas.")
    opcion = input("Por favor, ingrese el número correspondiente a la acción que desea realizar:\n1. Realizar la acción A (suma)\n2. Realizar la acción B (multiplicación)\nOpción: ")

    if opcion == '1':
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = accion_a(num1, num2)
        print(f"El resultado de la acción A (suma) es: {resultado}")
    elif opcion == '2':
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = accion_b(num1, num2)
        print(f"El resultado de la acción B (multiplicación) es: {resultado}")
    else:
        print("Opción no válida. Por favor, ingrese 1 o 2.")

if __name__ == "__main__":
    main()
