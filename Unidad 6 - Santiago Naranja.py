#Ejercicio 1

def imprimir_hola_mundo():
    return "Hola Mundo!"

print(imprimir_hola_mundo())

#Ejercicio 2

def saludar_usuario(nombre):
    return print(f"Hola {nombre}!")

nombre= input("Por favor ingresar su nombre: ")
saludar_usuario(nombre)


#Ejercicio 3

def informacion_personal(nombre, apellido, edad, residencia):
    return print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

nombre= input("Por favor ingresar su nombre: ")
apellido= input("Por favor ingresar su apellido: ")
edad= input("Por favor ingresar su edad: ")
residencia= input("Por favor ingresar su residencia: ")
informacion_personal(nombre, apellido, edad, residencia)


#Ejercicio 4

def informacion_personal(nombre, apellido, edad, residencia):
    return print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

nombre= input("Por favor ingresar su nombre: ")
apellido= input("Por favor ingresar su apellido: ")
edad= input("Por favor ingresar su edad: ")
residencia= input("Por favor ingresar su residencia: ")
informacion_personal(nombre, apellido, edad, residencia)

#Ejercicio 5

def segundos_a_horas(segundos):
    return print(f"El valor en horas es {segundos/3600}")

seg= int(input("Ingresar los segundos: "))
segundos_a_horas(seg)

#Ejercicio 6

def tabla_multiplicar(numero):
    for i in range(10):
        print(f"{i+1} x {numero} = {(i+1)*numero}")
    return 

num= int(input("Ingresar el numero que queres ver su tabla de multiplicación: "))
tabla_multiplicar(num)

#Ejercicio 7

def operaciones_basicas(num1,num2):
    operaciones= []
    print(f"El numero {num1} x {num2}  es {num1*num2}")
    operaciones.append(num1*num2)
    
    print(f"El numero {num1} + {num2}  es {num1+num2}")
    operaciones.append(num1+num2)
    
    print(f"El numero {num1} - {num2}  es {num1-num2}")
    operaciones.append(num1-num2)
    
    print(f"El numero {num1} / {num2}  es {num1/num2}")
    operaciones.append(num1/num2)
        
    return  tuple(operaciones)

num1= int(input("Ingresar el primer numero: "))
num2= int(input("Ingresar el segundo numero: "))
operaciones_basicas(num1,num2)

#Ejercicio 8

def calcular_imc(peso, altura):
    
    IMC= peso/altura*altura 
       
    return IMC

num1= float(input("Ingresar el peso en kgs: "))
num2= float(input("Ingresar la altura en metros: "))
IMC= calcular_imc(num1,num2)
print(f"Su indice de masa corporal es {IMC}")

#Ejercicio 9

def celsius_a_fahrenheit(celsius):
    
    
    Faren = (celsius*1.8) + 32.
    return Faren

num1= float(input("Ingresar la temperatura en Celsius: "))

Faren= celsius_a_fahrenheit(num1)

print(f"Su temperatura en Farenheit es {Faren}")


#Ejercicio 10

def calcular_promedio(a, b, c):
    
    
    promedio = (a + b + c)/3
    return promedio


num1= float(input("Ingresar el primer numero: "))
num2= float(input("Ingresar el segundo numero: "))
num3= float(input("Ingresar el tercer numero: "))
promedio=calcular_promedio(num1,num2,num3)

print(f"El promedio de los 3 numeros es: {promedio}")