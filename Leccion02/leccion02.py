# video 24 Operador aritmeticos en python
operandoA = 3
operandoB = 2
suma = operandoA + operandoB
#print('Resultado de la suma es:' , suma)
print(f'Resultado de la suma es: {suma}')


#Video 25 Operadores Aritmeticos en python - parte 2
resta = operandoA - operandoB
print(f'Resultado resta: {resta}')

multiplicacion = operandoA * operandoB
print(f'Resultado Multiplicacion: {multiplicacion}')

division = operandoA / operandoB
print(f'Resultado división: {division}')

division = operandoA // operandoB
print(f'Resultado division en (int): {division}')

modulo = operandoA % operandoB
print(f'Resultado residuo divison (modulo): {modulo}')

exponente = operandoA ** operandoB
print(f'Resultado exponente: {exponente}')

#Video 26 Ejercicio Propuesto Rectangulos

alto = int(input("Proporciona el alto del rectangulo: "))
ancho = int(input("Proporciona el ancho del rectangulo: "))
area = alto * ancho
perimetro = (alto + ancho) * 2

print(f'Area = {area}')
print(f'Perimetro = {perimetro}')