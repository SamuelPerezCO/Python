edad = int(input("Proporciona tu edad: "))

mensaje = None

if 0 <= edad < 10:
    mensaje = 'La infancia es Increible'
elif 10 <= edad < 20:
    mensaje = 'Muchos Cambios y mucho estudio'
elif 20 <= edad < 30:
    mensaje = 'Amor y comienza el trabajo'
else:
    mensaje = 'Etapa de vida no reconocida'

print(f'Para la edad {edad} el mensaje es {mensaje}')