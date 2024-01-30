class Persona:
    def __init__(self , nombre , apellido , edad):
        self._nombre = nombre
        self.apellido = apellido
        self.edad = edad

    @property
    def nombre(self):
        return self._nombre
    
    # @nombre.setter
    # def nombre(self , nombre):
    #     self._nombre = nombre

    def mostrar_detalle(self):
        print(f'Persona: {self._nombre} Apellido: {self.apellido} Edad: {self.edad}')

persona1 = Persona('Juan' , 'Perez' , 28 )
persona1.nombre = 'Juan Carlos'
print(persona1.nombre)