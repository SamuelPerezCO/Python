def imprimirNumeros(numero):
    if numero == 1:
        return print(1)
    else:
        print(numero)
        return imprimirNumeros(numero - 1)
 
numero = int(input("Ingrese el numero a restar: "))
imprimirNumeros(numero)