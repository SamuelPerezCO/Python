class Cubo:
    def __init__(self , ancho , profundo , alto):
        self.ancho = ancho
        self.profundo = profundo
        self.alto = alto

    def calcularVolumen(self):
        return self.ancho * self.profundo * self.alto
    
ancho = int(input("Proporcione el ancho del cubo: "))
profundo = int(input("Proporcione lo profundo del cubo: "))
alto = int(input("Proporcion el alto del cubo: "))

volumen = Cubo(ancho = ancho , profundo = profundo , alto = alto)
print(f'El volumen del cubo es: {volumen.calcularVolumen()}')