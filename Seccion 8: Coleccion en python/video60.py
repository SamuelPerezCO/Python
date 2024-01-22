nombres = ['Juan' , 'Karla' , 'Ricardo' , 'Maria']
#imprimir 
print(nombres)
#acceder a los elementos de una lista
print(nombres[0])
print(nombres[1])
#Acceder a los elementos de una lista de manera inversaa
print(nombres[-1])
print(nombres[-2])
#Imprimir un rango
print(nombres[0:2]) #Sin incluir el indice 2
#Ir del inicio de la lista al indice (sin incluirlo)
print(nombres[:3])
#Desde el indice indicado hasta el final 
print(nombres[1:])
#Cambiar un valor
nombres[3] = 'Ivone'
print(nombres)
#Iterar una lista
for nombre in nombres:
    print(nombre)
else:
    print("No existen mas nombres en la lista")