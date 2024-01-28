def multip(*args):
    resultado = 1
    for i in args:
        resultado *= i

    
    return resultado

print(f'El resultado de la multiplicacion es: {multip(3,5,15)}')