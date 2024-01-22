#Dada la siguiente tupla 
#Crear una lista que solo incluya los numeros menores a 5
lista = [ ]
tupla = (13 , 1 , 8 , 3 , 2 , 5 , 8)
for i in tupla:
    if i < 5:
        lista.append(i)
        
print(lista)