class Persona:
    def __init__(self , nombre , apellido , edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    
    def mostrar_detalle(self):
        print(f'Persona: {self.nombre} Apellido: {self.apellido} Edad: {self.edad}')

persona1 = Persona('Juan' , 'Perez' , 28)
persona1.mostrar_detalle()

persona2 = Persona('Karla' , 'Gomez' , 30)
persona2.mostrar_detalle()