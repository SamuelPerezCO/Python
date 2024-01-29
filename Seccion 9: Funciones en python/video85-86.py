def impuesto(dinero , porcentaje_impuesto):
    pImpuesto = dinero + dinero * (porcentaje_impuesto / 100)
    return pImpuesto

dinero = int(input("Proporcione el pago sin impuesto: "))
porcentaje_impuesto = int(input("Proporcione el monto del impuesto: "))

print(impuesto(dinero , porcentaje_impuesto))