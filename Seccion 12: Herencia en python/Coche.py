from Vehiculo import *

class coche(Vehiculo):

    def __init__(self, color, ruedas , velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad

    @property
    def velocidad(self):
        return self.velocidad

    def __str__(self):
        return f'{super().__str__()} Velocidad: {self.velocidad}'
    
carro = coche("Negro" , 4 , 10)
print(carro)