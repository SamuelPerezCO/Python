class Aritmetica:
    """
    Clase Aritmetica para realizar las operacion de sumar , restar , etc
    """
    def __init__(self, operandoA, operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB

    def sumar(self):
        return self.operandoA + self.operandoB

aritmetica1 = Aritmetica(5,3)
print(aritmetica1.sumar())