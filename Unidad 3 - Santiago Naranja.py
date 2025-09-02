#Ejercicio 1

edad= int(input("Por favor ingresar su edad: "))

if edad>18:
    print("Es mayor de edad")
else:
    pass


#Ejercicio 2

nota= int(input("Por favor ingresar su nota: "))

if nota>=6:
    print("Aprobado")
else:
    print("Desaprobado")


#Ejercicio 3

numero= int(input("Por favor ingresar un numero par: "))

if numero%2 ==0:
    print("Ha ingresado un numero par")
else:
    print("Por favor, ingrese un número par")

#Ejercicio 4

edad= int(input("Por favor ingresar usu edad: "))

if edad<12:
    print("Niño/a")
elif(edad>=12 and edad<18):
    print("Adolescente")
elif (edad>=18 and edad<30):
    print("Adulto/a joven")
else:
    print("Adulto/a")

#Ejercicio 5

contrasena= input("Por favor ingresar su contraseña: ")

if len(contrasena)>=8 and len(contrasena)<=14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#Ejercicio 6

import random
from statistics import mode, median, mean

numeros_aleatorios = [random.randint(1,100) for i in range(50)]

moda= mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

if media>mediana and mediana>moda:
    print("Sesgo positivo o a la derecha")
elif media<mediana and mediana<moda:
    print("Sesgo negativo o a la izquierda")
elif media==mediana and mediana==moda:
    print("Sin sesgo")
    
    

#Ejercicio 7

frase= input("Ingresar frase o palabra: ")
ultima_letra= frase[-1]

if ultima_letra=="a" or ultima_letra=="e" or ultima_letra=="i" or ultima_letra=="o" or ultima_letra=="u":
    print(f"{frase}!")
else:
     print(f"{frase}")

#Ejercicio 8

nombre= input("Ingrese su primer nombre: ")
opcion=int(input("Ingrese alguna de estas opciones: 1. Si quiere su nombre en mayúsculas. - 2. Si quiere su nombre en minúsculas. - 3. Si quiere su nombre con la primera letra mayúscula.")) 


if opcion==1:
    mayuscula= nombre.upper()
    print(f"{mayuscula}")
elif opcion==2:
    minuscula= nombre.lower()
    print(f"{minuscula}")
elif opcion==3:
    solo_un_mayuscula= nombre.title()
    print(f"{solo_un_mayuscula}")
else:
    print("Tenes que ingresar 1, 2 o 3")

#Ejercicio 9

terremoto=int(input("Ingrese la magnitud del terremoto: ")) 

if terremoto<3:
    print("Muy leve (imperceptible)")
elif terremoto>=3 and terremoto<4:
    print("Leve (ligeramente perceptible)")
elif terremoto>=4 and terremoto<5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif terremoto>=5 and terremoto<6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif terremoto>=6 and terremoto<7:
    print("Muy Fuerte (puede causar daños significativos)")  
else:
    print("Extremo (puede causar graves daños a gran escala)") 

#Ejercicio 10

hemisferio=input("Ingrese el hemisferio en el que se encuentra N o S para Norte o Sur, segun corresponda: ").lower() 
mes=input("Ingrese el mes del año en letras: ").lower()
dia=int(input("Ingrese el dia del año: "))

if hemisferio.lower()=="n":
    if (dia>=21 and mes.lower()=="diciembre") or (mes.lower()=="enero") or (mes.lower()=="febrero") or (mes.lower()=="marzo" and dia<=20):
        print("Invierno")
    elif (dia>=21 and mes.lower()=="marzo") or (mes.lower()=="abril") or (mes.lower()=="mayo") or (mes.lower()=="junio" and dia<=20):
        print("Primavera")
    elif (dia>=21 and mes.lower()=="junio") or (mes.lower()=="julio") or (mes.lower()=="agosto") or (mes.lower()=="septiembre" and dia<=20):
        print("Verano")
    elif (dia>=21 and mes.lower()=="septiembre") or (mes.lower()=="octubre") or (mes.lower()=="noviembre") or (mes.lower()=="diciembre" and dia<=20):
        print("Otoño")
else:
    if (dia>=21 and mes.lower()=="diciembre") or (mes.lower()=="enero") or (mes.lower()=="febrero") or (mes.lower()=="marzo" and dia<=20):
        print("Verano")
    elif (dia>=21 and mes.lower()=="marzo") or (mes.lower()=="abril") or (mes.lower()=="mayo") or (mes.lower()=="junio" and dia<=20):
        print("Otoño")
    elif (dia>=21 and mes.lower()=="junio") or (mes.lower()=="julio") or (mes.lower()=="agosto") or (mes.lower()=="septiembre" and dia<=20):
        print("Invierno")
    elif (dia>=21 and mes.lower()=="septiembre") or (mes.lower()=="octubre") or (mes.lower()=="noviembre") or (mes.lower()=="diciembre" and dia<=20):
        print("Primavera") 