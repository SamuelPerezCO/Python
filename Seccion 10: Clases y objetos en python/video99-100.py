class Area:
    def __init__(self , base , altura):
        self.base = base
        self.altura = altura

    def definirArea(self):
        return self.base * self.altura
    
base = int(input("Proporcione la base: "))
altura = int(input("Proporcione la altura: "))

area1 = Area(base , altura)
print(f' Area Rectangulo: {area1.definirArea()}')