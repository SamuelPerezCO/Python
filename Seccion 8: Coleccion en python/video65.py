#Definir una tupla
frutas = ('Naranja' , 'Platano' , 'Guayaba')
print(frutas)
#Saber el largo 
print(len(frutas))
#acceder a un elemento
print(frutas[0])
#Navegacion Inversa
print(frutas[-1])
#Acceder a un rango 
print(frutas[0:2]) # Sin incluir el ultimo indice
#Recorrer elementos 
for fruta in frutas:
    print(fruta , end=' ') #para que se cambie la forma de imprimir los elementos
#Cambiar valor tupla
#frutas[0] = 'Pera'
frutasLista = list(frutas) #Para cambiar a una lista
frutasLista[0] = 'Pera'
frutas = tuple(frutasLista)
print('\n',frutas)
#Eliminar tupla por completo
del frutas