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