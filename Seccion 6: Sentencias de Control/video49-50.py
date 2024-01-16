valor = int(input('Proporcione un valor entre 0 y 10: '))
calificacion = None

if 0 <= valor < 6:
    calificacion = 'F'
elif 6 <= valor < 7:
    calificacion = 'D'
elif 7 <= valor < 8:
    calificacion = 'C'
elif 8 <= valor < 9:
    calificacion = 'B'
elif 9 <= valor <= 10:
    calificacion = 'A'
else:
    calificacion = 'Valor Incorrecto'

print(f'La calificacion para {valor} es {calificacion}')