"""
De ahora en adelante no se llamaron video tal video tal si no solo la carpeta y lo que se desarrolle 
asi se ve mas organizado y poder realizar el proyecto que realiza el y manejarlo mejor
"""
class Persona:
    def __init__(self , nombre , edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f'Persona: Nombre -> {self.nombre} Edad -> {self.edad}'

class Empleado(Persona):
    def __init__(self , nombre , edad, sueldo):
        super().__init__(nombre , edad)
        self.sueldo = sueldo

    def __str__(self):
        return f'{super().__str__()} Sueldo: {self.sueldo}'