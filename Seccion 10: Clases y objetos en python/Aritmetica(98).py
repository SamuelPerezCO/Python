class Aritmetica:
    """
    Clase Aritmetica para realizar las operacion de sumar , restar , etc
    """
    def __init__(self, operandoA, operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB

    def sumar(self):
        return self.operandoA + self.operandoB
    
    def restar(self):
        return self.operandoA - self.operandoB
    
    def multiplicar(self):
        return self.operandoA * self.operandoB
    
    def Dividir(self):
        return self.operandoA / self.operandoB

aritmetica1 = Aritmetica(5,3)

print(f'Suma: {aritmetica1.sumar()}')
print(f'Resta: {aritmetica1.restar()}')
print(f'Multiplicacion: {aritmetica1.multiplicar()}')
print(f'Dividir: {aritmetica1.Dividir():.2f}')