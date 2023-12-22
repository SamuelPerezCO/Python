#Enviar un salido a la consola utilizando python
print("Este es mi Saludo desde python")
print("=" * 50)
#Video 8 (No han creado otra carpeta)
miVariable = 2
print(miVariable)
print(miVariable)
print(miVariable)

miVariable = 10
print(miVariable)
print("=" * 50)
#Video 9 
x = 10 
y = 2
z = x + y
print("Valor de x = " , x)
print("Valor de y = " , y)
print("Valor de z = " , z)
print("=" * 50)

#Video 10 (Direccion de memoria y variables en python)
print("La direccion en memoria de x es = " , id(x))
print("La direccion en memoria de y es = " , id(y))
print("La direccion en memoria de z es = " , id(z))
print("=" * 50)
#Video 11 y 12 (Ejercicio Propuesto Uso de Variables)
#Declaracion de variables
nombre = "Juan Perez"
numero = 55621817
gmail = "jperez@gmail.com"

print("El nombre es =" , nombre)
print("El numero es = " , numero)
print("El correo es = " , gmail)

print("=" * 50)
#Video 13 (Tipos de datos en python)
x = 10 
print("La variable x tiene contenido de: " , x)
print("El tipo de dato de x es =" , type(x))

x = 'Hola mundo' 
print("La variable x tiene contenido de: " , x)
print("El tipo de dato de x es =" , type(x))

y: str = "Hola mundo 2"
print("La variable y tiene un contenido de :" , y)
print("El tipo de dato de y es: " , type(y)) 

z = True
print("La variable z tiene contenido de: " , z)
print("El tipo de dato de z es =" , type(z))

print("=" * 50)

#Video 14 (Resumen tipos de datos en python)
#Tipo Int
x = 10 
print(x)
print(type(x))
#Tipo float
x = 14.5
print(type(x))
#Tipo String
x = "Hola mundo"
print(type(x))
#Tipo Boolean
x = True
print(type(x))
x = False
print(type(x))

print("=" * 50)

#Video 15 (Manejo de cadenas en python)
#Cadena (String)

miGrupoFavorito = "Metallica"
comentario = "The Best Rock Band"
print("Mi grupo Favorito es = " + miGrupoFavorito + " " + comentario)

print("=" * 50)

#Video 16 (Mas temas de manejo de cadenas)
print("Mi grupo favorito es: " , miGrupoFavorito , comentario)

numero1 = "1"
numero2 = "2"
print( "La concatenacion de las dos variables es: ",numero1 + numero2)
print("La suma de la conversion de los numero es: " , int(numero1) + int(numero2))

numero1 = 1
numero2 = 2
print("La suma de las dos variables es: ",numero1 + numero2)

print("=" * 50)

# Video 17 (TIpos Boleanos (bool) en python)
# Tipos Bool (boolean)

miVariable = True
print(miVariable) 

miVariable = 3 > 2
print(miVariable)

if miVariable:
    print("El resultado fue verdadero")
else:
    print("El resultado fue falso")

print("=" * 50) 

#Video 18 (Procesar entrada del usuario(Funcion Input))
#Funcion input

resultado = "Ingresa un mensaje" #Aqui tendria un input pero lo quite para poder tener la ejecuccion del programa mas rapido
print("El valor suministrado fue:" , resultado)
print("Fin del programa")
print("=" * 50) 

# Video 19 (Conversion de la entrada de datos en python)
#Funcion input para procesar la entrada del usuario

numero1 = "Ingrese el primer numero: " #Aqui tendria un input pero lo quite para poder tener la ejecuccion del programa mas rapido
numero2 = "Ingrese el segundo numero: "#Aqui tendria un input pero lo quite para poder tener la ejecuccion del programa mas rapido
resultado = numero1 + numero2
print("El resultado de la suma es: " , resultado) 

print("=" * 50)

#Video 20 y 21 (Ejercicio califica tu dia)
#Califica tu dia de 1 al 10 

calificacion = "Califica tu dia (1 al 10)" #Aqui tendria un input pero lo quite para poder tener la ejecuccion del programa mas rapido
print("Mi dia estuvo de: " , calificacion)

print("=" * 50)

#Video 22(Ejercicio propuestyo Detalles de un libro)
titulo = input("Proporciona el titulo del libro: ")
autor = input("Proporciona el auto del libro: ")
print(titulo , "Fue escrito por ", autor)
