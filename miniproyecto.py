import os

print("Bienvenido a su cajero virtual")


menu=input(" Seleccione una opcion entre (1-4): \n1.Consultar saldo \n2.Depositar dinero \n3.Retirar dinero \n4. Salir \n")

match menu:
    case "1": 
        print("Su saldo inicial es de: $100000")
        input("pause")
    case "2":
        pass
    case _:
        pass