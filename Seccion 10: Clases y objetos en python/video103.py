class Persona:
    def __init__(self , nombre , apellido , edad , *valores , **terminos):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.valores = valores
        self.terminos = terminos
    
    def mostrar_detalle(self):
        print(f'Persona: {self.nombre} Apellido: {self.apellido} Edad: {self.edad} Valores: {self.valores} Terminos: {self.terminos}')

persona1 = Persona('Juan' , 'Perez' , 28 , '44638734' , 2 , 3 , 5 , m='manzana' , p='pera')
persona1.mostrar_detalle()


persona2 = Persona('Karla' , 'Gomez' , 30)
persona2.mostrar_detalle()