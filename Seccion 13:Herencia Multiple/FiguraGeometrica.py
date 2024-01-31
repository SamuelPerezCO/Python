class FiguraGeometrica:
    def __init__(self , ancho , alto):
        self.ancho = ancho
        self.alto = alto

    @property
    def alto(self):
        return self.alto
    
    @alto.setter
    def alto (self , alto):
        self.alto = alto

    @property
    def ancho(self , ancho):
        self.ancho = ancho