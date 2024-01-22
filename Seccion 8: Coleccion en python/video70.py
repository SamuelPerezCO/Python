#Dict (key , value)
diccionario = {
    'IDE' : 'Integrated Development Environment' ,
    'OOP' : 'Object Oriented Programming',
    'DBMS' : 'Database Management System' 
}
print(diccionario)
#Largo 
print(len(diccionario))
#acceder a un elemento (key)
print(diccionario['IDE'])
#Otra forma de recuperar un elemento
print(diccionario.get('OOP'))
#Modificando elementos
diccionario['IDE'] = 'integrated development environment'
print(diccionario)
#Recorrer los elementos
for termino , valor in diccionario.items(): #.items para imprimir el value del diccionario y se pone la otra variable para recorrer el value
    print(termino , valor)

for termino in diccionario.keys(): #para imprimir solo las llaves sin el termino asociado
    print(termino)

for valor in diccionario.values(): #Para imprimir solo los valores del diccionario
    print(valor)

#Comprobar existensia de algun elemento
print('IDE' in diccionario)

#agregar un elemento 
diccionario['PK'] = 'Primary Key'
print(diccionario)

#Remover un elemento
diccionario.pop('DBMS')
print(diccionario)

#limpiar
diccionario.clear()
print(diccionario)

#Eliminar la variable por compleo
del diccionario
