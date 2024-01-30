from Vehiculo import *

class Bicicleta(Vehiculo):

    def __init__(self, color, ruedas , tipo):
        super().__init__(color, ruedas)
        self._tipo = tipo

    @property
    def tipo(self):
        return self.tipo
    
    def __str__(self ):
        return f'{super().__str__()} Tipo: {self.tipo}'

bicicleta1 = Bicicleta("Amarilla" , 3 , "Montaña")
print(bicicleta1)