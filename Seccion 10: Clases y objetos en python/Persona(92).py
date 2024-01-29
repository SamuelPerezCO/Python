class Persona:
    def __init__(self , nombre , apellido , edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

persona1 = Persona('Juan' , 'Perez' , 28)
print(f'Objeto Persona 1 Nombre: {persona1.nombre} Apellido: {persona1.apellido} Edad: {persona1.edad}')

persona2 = Persona('Karla' , 'Gomez' , 30)
print(f'Objeto Persona 2 Nombre: {persona2.nombre} Apellido:{persona2.apellido} Edad: {persona2.edad}')