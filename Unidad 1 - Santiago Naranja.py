#Ejercicio 1

print("Hola Mundo!")

#Ejercicio 2
nombre= input("Por favot ingrese su nombre: ")
print(f"Hola {nombre}!")

#Ejercicio 3
nombre= input("Por favot ingrese su nombre: ")
apellido= input("Por favot ingrese su apellido: ")
edad= input("Por favot ingrese su edad: ")
residencia= input("Por favot ingrese su lugar de residencia: ")


print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

 

#Ejercicio 4
import math

radio= float(input("Por favot ingrese el radio del circulo: "))
area= math.pi * radio**2
perimetro = 2 * math.pi * radio

print(f"Su area es {area}")
print(f"Su perimetro es {perimetro}")

#Ejercicio 5
segundos= int(input("Por favor ingrese la cantidad de segundos: "))
horas = segundos/60/60

print(f"Esos segundos equivalen a {horas} horas")

#Ejercicio 6
numero= int(input("Por favor ingrese un numero: "))
numeroporcero= numero*0
numeroporuno= numero*1
numeropordos= numero*2
numeroportres= numero*3
numeroporcuatro= numero*4
numeroporcinco= numero*5
numeroporseis= numero*6
numeroporsiete= numero*7
numeroporocho= numero*8
numeropornueve= numero*9
numeropordiez= numero*10

print(f"El {numero} por cero es {numeroporcero}")
print(f"El {numero} por uno es {numeroporuno}")
print(f"El {numero} por dos es {numeropordos}")
print(f"El {numero} por tres es {numeroportres}")
print(f"El {numero} por cuatro es {numeroporcuatro}")
print(f"El {numero} por cinco es {numeroporcinco}")
print(f"El {numero} por seis es {numeroporseis}")
print(f"El {numero} por siete es {numeroporsiete}")
print(f"El {numero} por ocho es {numeroporocho}")
print(f"El {numero} por nueve es {numeropornueve}")
print(f"El {numero} por diez es {numeropordiez}")


#Ejercicio 7
numero1= int(input("Por favor ingrese un numero distinto de cero: "))
numero2= int(input("Por favor ingrese otro numero distinto de cero: "))

suma= numero1 + numero2
resta= numero1 - numero2
division = numero1 / numero2
multiplicacion = numero1 * numero2

print(f"La suma de los numeros es {suma}")
print(f"La resta de los numeros es {resta}")
print(f"La division de los numeros es {division}")
print(f"La multiplicacion de los numeros es {multiplicacion}")

#Ejercicio 8

peso= float(input("Por favor ingrese su peso en kg: "))
altura= float(input("Por favor ingrese su altura en metros: "))

IMC = peso/altura

print(f"Su indice de masa corporal es {IMC}")

#Ejercicio 9
temperatura= float(input("Por favor ingrese su temperatura en Celsius: "))

Fahrenheit = 9/5 * temperatura + 32

print(f"Su temperatura en Fahrenheit es {Fahrenheit}")

#Ejercicio 10

numero1= int(input("Por favor ingrese un numero: "))
numero2= int(input("Por favor ingrese otro numero: "))
numero3= int(input("Por favor ingrese otro numero: "))

promedio = (numero1 + numero2 + numero3)/3

print(f"El promedio de los tres numeros es {promedio}")

