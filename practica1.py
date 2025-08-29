import os

isActive=True
while isActive:
    os.system("clear")
    print("Bienvenido al generador de triangulos")
    try:
        n = int(input("Ingrese la cantidad de la base del triangulo \n o ingrese 0 para salir: "))
        if n == 0:
            isActive = False
            print("Gracias por usar el programa")
        elif n > 1:
            for i in range(1, n+1):
                print("*" * i)
            input("pause")
        else:
            print("No existe un triangulo con base 1")
            input("pause")
    except: ValueError
    print("Debe ingresar un numero entero")