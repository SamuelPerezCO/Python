#set
planetas = {'Marte' , 'Jupiter' , 'Venus'}
print(planetas)
#largo 
print(len(planetas))
# revisar si un elemento esta presente
print('Marte' in planetas)
#Agregar un elemento
planetas.add('Tierra')
print(planetas)
#no se pueden duplicar elementos
planetas.add('Tierra')
print(planetas)
#eliminar un elemento posiblemente arrojando un error
planetas.remove('Tierra')
print(planetas)
#eliminar elemento sin arrojar error
planetas.discard('Jupiter')
print(planetas)
#Limpiar por completo 
planetas.clear()
print(planetas)
#eliminar por completo
del planetas