from Cuadrado import Cuadrado
from Rectangulo import *


print('Creacion Objecto Cuadrado'.center(50,'-'))
cuadrado1 = Cuadrado(lado = 5 , color= 'rojo')

print(f'Calculo area cuadrado: {cuadrado1.calcular_area()}')

print(cuadrado1)
print('Creacion Objecto Rectangulo'.center(50,'-'))
rectangulo1 = Rectangulo(ancho = 3 , alto = 2 , color = "Verde")
print(f'Calculo are Rectangulo {rectangulo1.calcular_area()}')
print(rectangulo1)