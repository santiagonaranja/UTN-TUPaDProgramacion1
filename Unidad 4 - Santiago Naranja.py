#Ejercicio 1

for i in range(0,101):
    print(i," ")

#Ejercicio 2

numero = str(input("Ingrese un numero entero: "))
contador = 0

for i in numero:
    contador+=1
    
print("EL numero tiene ", contador, " digitos")



#Ejercicio 3


numero1 = int(input("Ingrese el primer numero entero: "))
numero2 = int(input("Ingrese el segundo numero entero: "))

suma = 0

if numero1 > numero2:
    for i in range(numero2+1,numero1):
        suma =+ i + suma
    print(f"La suma de todos los numeros entre {numero1} y {numero2} es {suma}")
elif numero2 > numero1:
    for i in range(numero1+1,numero2):
        suma =+ i + suma
    print(f"La suma de todos los numeros entre {numero2} y {numero1} es {suma}")
else:
    print("Ingresaste el mismo numero")

#Ejercicio 4


numero = int(input("Ingrese el primer numero entero: "))
suma = 0

while numero != 0:
    suma =+numero + suma
    numero = int(input("Ingrese el primer numero entero: "))
    
print(f"La suma de todos los numeros es {suma}")

#Ejercicio 5

import random
numero = int(input("Ingrese un numero al azar: "))
suma = 1
random1 = random.randint(0,9)

while numero != random1:
    suma =+ 1 + suma
    numero = int(input("Ingrese un numero al azar: "))
    
print(f"la cantidad de intentos para adivinar el numero fueron {suma}")

#Ejercicio 6
for i in range(100,-2,-2):
    print(i, end=" ")
    
#Ejercicio 7


numero = int(input("Ingrese un numero entero positivo: "))
suma = 0

for i in range(0,numero +1):
    suma +=i
    
print(f"La suma de todos los numeros comprendidos entre 0 y {numero} es {suma}")


#Ejercicio 8
suma_pares = 0
suma_impares = 0
suma_positivos = 0
suma_negativos = 0

for i in range(0,101):
    numero = int(input("Ingrese un numero entero: "))
    if numero % 2 == 0:
        suma_pares += 1
    if numero % 2 != 0:
        suma_impares += 1
    if numero >= 0:
        suma_positivos += 1
    if numero <= 0:
        suma_negativos += 1
    
print(f"La suma de todos los numeros pares son {suma_pares}")
print(f"La suma de todos los numeros impares son {suma_impares}")
print(f"La suma de todos los numeros negativos son {suma_negativos}")
print(f"La suma de todos los numeros positivos son {suma_positivos}")

#Ejercicio 9

numero = int(input("Ingrese un numero entero: "))
suma = 0
contador= 0

for i in range(0,4):
    suma+= numero
    contador+=1
    numero = int(input("Ingrese un numero entero: "))
    
print("La media de esos valores es:  ", suma/contador)

#Ejercicio 10


numero = str(input("Ingrese un numero entero: "))


for i in range(len(numero) - 1, -1, -1):
    print (numero[i], end="")
    
