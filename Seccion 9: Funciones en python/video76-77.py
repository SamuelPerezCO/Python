def suma(*args):
    sum = 0
    for i in args:
        sum += i
        
    return sum
    
print(f'El resultado de la suma es:{suma(1 , 2 , 4 ,1 ,5)}')
