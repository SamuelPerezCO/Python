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
"""
alto = int(input("Proporciona el alto del rectangulo: "))
ancho = int(input("Proporciona el ancho del rectangulo: "))
area = alto * ancho
perimetro = (alto + ancho) * 2

print(f'Area = {area}')
print(f'Perimetro = {perimetro}')
"""

#Video 28 Operadores de asignacion
miVariable = 10
print(miVariable)

miVariable = miVariable + 1
print(miVariable)
#Incremento con reasignacion
miVariable += 1
print(miVariable)

miVariable -= 2
print(miVariable)

miVariable *= 3
print(miVariable)

miVariable /= 2
print(miVariable)

#Video 29 Operadodes de comparacion

a = 4

b = 2

resultado = a == b
print(f'Resultado ==: {resultado}')

resultado = a != b
print(f'Resultado != {resultado}')

resultado = a > b
print(f'Resultado > : {resultado}')

resultado = a >= b
print(f'Resultado >= : {resultado}')

resultado = a < b 
print(f'Resultado < : {resultado}')

resultado = a <= b
print(f'Resultado <= : {resultado}')
"""
#Video 30 Numero impar o par 
a = int(input("Ingrese un numero: "))

resultado = (a % 2)

if resultado == 0:
    print(f'{a} , es un numero par')
else:
    print(f'{a} , no es un numero par')

#Video 31 Determina si es mayor de edad
    
a = int(input("Ingrese una edad: "))

if a >= 18:
    print(f'{a} , es mayor de edad')
else:
    print(f'{a} , no es mayor de edad')
"""
#Video 32 Operadores logicos en python

a = True 
b = True 
resultado = a and b
print(resultado)

resultado = a or b
print(resultado)

resultado = not a
print(resultado)

#Video 33 Ejercicio - Valor dentro de un rango (and)
"""
a = int(input("Ingrese un numero: "))

if a >= 0 and a <= 5:
    print(f'El numero {a} si esta en el rango de 0 a 5')
else:
    print(f'El numero {a} , no esta en el rango de 0 a 5')
"""

#Video 34 Ejercicio - Operador Or

vacaciones = False
diaDescanso = True

if vacaciones or diaDescanso:
    print("Puede asistir al juego")
else:
    print("No puede asistir al juego")

#Video 35 Ejericio Operador not

vacaciones = False
diaDescanso = True

if not(vacaciones or diaDescanso):
    print("No puede asistir al juego")
else:
    print("Puede asistir al juego")

#Video 36 Ejercicio - Rango entre 20 y 30
edad = 22 #int(input("Ingrese la edad: "))

veintes = edad >= 20 and edad < 30
treintas = edad >= 30 and edad < 40

if veintes or treintas:
    print(f"la edad {edad} esta correcta")
else:
    print(f"La edad {edad} esta incorrecta")

#Video 37 Sintaxis Simplificada Operador and

if (20 <= edad < 30) or (30 <= edad < 40):
    print(f"Si esta en el rango de 20's y 30's , Edad es: {edad}")
else:
    print(f"No esta en el rango de 20's y 30's , Edad es: {edad}")

#Video 38 el mayor de dos numeros

n1 = 1 #int(input("Ingrese el numero 1: "))
n2 = 3 #int(input("Ingrese el numero 2: "))

if n1 > n2:
    print(f"El numero mayor es: {n1}")
else:
    print(f"El numero mayor es: {n2}")

#Video 40 Ejercicio - Tienda de libros
print("Proporcione los siguientes datos del libro:")
nombreLibro = input("Proporcione el nombre: ")
id = int(input("Proporcione el Id: "))
precio = float(input("Proporcione el precio: "))
envio = input("Indica si el envio es gratuito (True/False): ")

print("=" * 50)
print(f"El nombre del libro es: {nombreLibro}")
print(f"El id del libro es: {id}")
print(f"El precio del libro es: {precio}")
print(f"El envio es gratuito: {envio}")
print("=" * 50)