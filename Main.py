import Operaciones
import os

while True:
    a = float(input("Ingresa el primer número: "))
    b = float(input("Ingresa el segundo número: "))

    print("¿Qué operación deseas realizar?")
    print("a) Suma")
    print("b) Resta")
    print("c) Multiplicación")
    print("d) División")

    operacion = input("Elige una opción (a/b/c/d): ")

    if operacion == "a":
        resultado = Operaciones.suma(a, b)
    elif operacion == "b":
        resultado = Operaciones.resta(a, b)
    elif operacion == "c":
        resultado = Operaciones.multiplicacion(a, b)
    elif operacion == "d":
        resultado = Operaciones.dividir(a, b)
    else:
        resultado = "Opción no válida"

    print("Resultado:", resultado)

    continuar = input("\n¿Deseas realizar otra operación? (s/n): ")
    os.system('cls')

    if continuar != "s":
        print("¡Hasta luego!")
        break