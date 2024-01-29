def celsius_a_fahrenheit(celsius):
    return (9/5) * celsius + 32

def fahrenheit_a_celsius(fahrenheit):
    return (5/9) * (fahrenheit - 32)

temperatura_celsius = 25
temperatura_fahrenheit = celsius_a_fahrenheit(temperatura_celsius)
print(f"{temperatura_celsius} grados Celsius son {temperatura_fahrenheit:.2f} grados Fahrenheit")

temperatura_fahrenheit = 77
temperatura_celsius = fahrenheit_a_celsius(temperatura_fahrenheit)
print(f"{temperatura_fahrenheit} grados Fahrenheit son {temperatura_celsius:.2f} grados Celsius")