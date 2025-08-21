import math

radio= float(input("Por favot ingrese el radio del circulo: "))
area= math.pi * radio**2
perimetro = 2 * math.pi * radio

print(f"Su area es {area}")
print(f"Su perimetro es {perimetro}")