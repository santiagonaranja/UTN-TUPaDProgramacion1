#Ejercicio 1

notas = [4, 5, 6, 7, 7, 5, 8, 10, 9, 9]

cantidad_de_elementos= len(notas)
suma=0
mayor=float("-inf")
menor=float("inf")

for i in range(cantidad_de_elementos):
    suma= suma + notas[i]
    if notas[i] > mayor:
        mayor= notas[i]
    
    if notas[i] < menor:
        menor= notas[i]
              
print(f"La lista completa es: {notas}")
print(f"El promedio es: {suma/cantidad_de_elementos}")    
print(f"El mayor de la lista es: {mayor}")
print(f"El menor de la lista es: {menor}")

#Ejercicio 2



producto=[]

print("A continuacion ingresaras 5 productos:")
for i in range(5):
    producto.append(input(f"Por favor, ingresas el producto {i+1}: "))
    
producto_ordenado= sorted(producto)
print(f"La lista ordenada es: {producto_ordenado}")         
eliminar= input(f"Ingresar un producto que se quiere eliminar: ")
producto_ordenado.remove(eliminar)
print(f"La lista ordenada y con el producto elimnado es: {producto_ordenado}") 


#Ejercicio 3

import random

numeros=[]
pares=[]
impares=[]


for i in range(15):
    numeros.append(random.randint(1,100))
    
for i in range(15):
    
    if numeros[i] % 2 == 0:
        pares.append(numeros[i])
    
    if numeros[i] % 2 != 0:
        impares.append(numeros[i])


print(f"La lista original es: {numeros}") 
print(f"La lista de los pares tiene {len(pares)} numeros y es:  {pares}") 
print(f"La lista de los impares tiene {len(impares)} numeros y es:  {impares}") 

#Ejercicio 4


datos=[1, 3, 5, 3, 7, 1, 9, 5, 3]
sin_repetidos=[]

print(f"La lista original es: {datos}") 


for valor in datos:
    if valor not in sin_repetidos:
        sin_repetidos.append(valor)
        

print(f"La lista sin valores reperitdos es: {sin_repetidos}") 


#Ejercicio 5

estudiantes=[]

print("A continuacion ingresaras 8 estudiantes:")
for i in range(8):
    estudiantes.append(input(f"Por favor, ingresas el estudiante {i+1}: "))
    estudiantes[i].lower()

print(f"Los 8 estudiantes ingresados son: {estudiantes}")


respuesta=input("Queres eliminar algun estudiante? Ingresar si o no: ").lower()

if respuesta=="si":
    elim=input("A quien? ").lower()
    estudiantes.remove(elim)
    
respuesta=input("Queres agregar algun estudiante? Ingresar si o no: ").lower()

if respuesta=="si":
    agregar=input("Ingresar estudiante: ").lower()
    estudiantes.append(agregar)
    
print(f"La nueva lista de estudiantes es: {estudiantes}")

#Ejercicio 6


nume=[1, 3, 5, 76, 90, 100]
print(f"La lista de origen es: {nume}")

ultimo_elemento=nume.pop()
nume.insert(0,ultimo_elemento)

print(f"La lista corrida un numero a la derecha es: {nume}")


#Ejercicio 7


semana=[[25, 30], [20, 31], [17, 23], [15, 16], [23, 34], [14, 28], [27, 28]]
print(f"Las temperaturas son: {semana}")
suma_minima=0
suma_maxima=0
amplitud=0

for i in range(7):
    suma_minima= suma_minima + semana[i][0]
    suma_maxima= suma_maxima + semana[i][1]
    if semana[i][1] - semana[i][0] > amplitud:
        dia_amplitud= i+1 


print(f"El promedio de la temperatura minima es: {suma_minima/len(semana)}")
print(f"El promedio de la temperatura maxima es: {suma_maxima/len(semana)}")
print(f"El dia de la mayor amplitud termica es: {i}")

        


#Ejercicio 8


notas = [
    [7, 8, 9],   
    [5, 6, 7],   
    [9, 8, 10],  
    [4, 6, 5],   
    [8, 9, 7]    
]

print("Las notas de los estudiantes son:")
for fila in notas:
    print(fila)

print()

print("El promedio de cada estudiante es:")
for i, fila in enumerate(notas):
    promedio_est = sum(fila) / len(fila)
    print(f"Estudiante {i+1}: {promedio_est}")

print()

print("Promedio de cada materia: ")
num_estudiantes = len(notas)
num_materias = len(notas[0])

print()

for j in range(num_materias):
    suma_materia = 0
    for i in range(num_estudiantes):
        suma_materia += notas[i][j]
    promedio_mat = suma_materia / num_estudiantes
    print(f"Materia {j+1}: {promedio_mat}")


#Ejercicio 9


tablero = [
    ["-", "-", "-"],   
    ["-", "-", "-"],  
    ["-", "-", "-"]   
]

print("El tablero del Ta-Te-Ti:")
for turno in tablero:
    print(turno)
print()


for j in range(9):
    fila_x=int(input("Ingresar la fila donde quiere poner el jugador X: "))
    columna_x=int(input("Ingresar la columna donde quiere poner el jugador X: "))
    
    tablero[fila_x-1][columna_x-1]= "X"
    fila_O=int(input("Ingresar la fila donde quiere poner el jugador O: "))
    columna_O=int(input("Ingresar la columna donde quiere poner el jugador O: "))
    
    
    tablero[fila_O-1][columna_O-1]= "O"
    
    
    for turno in tablero:
        print(turno)
    print()


#Ejercicio 10

ventas = [
    [7, 8, 9, 10, 20, 25, 30],   
    [5, 6, 7, 7, 8, 9, 11],   
    [9, 8, 10, 7, 7, 8, 9],  
    [4, 6, 5, 9, 8, 10, 7]   
]

print("Las ventas de los productos son:")
for fila in ventas:
    print(fila)

print()

print("La venta de cada producto es: ")
producto_ganador=0
for i, fila in enumerate(ventas):
    venta_producto = sum(fila)
    print(f"Producto {i+1}: {venta_producto}")
    if venta_producto>producto_ganador:
        producto_ganador=venta_producto
        posicion_producto_ganador= i+1

print()


for j in range(7):
    suma_dia_ventas = 0
    suma_ganadora=0
    for i in range(4):
        suma_dia_ventas += ventas[i][j]
    if suma_dia_ventas>suma_ganadora:
        suma_ganadora=suma_dia_ventas
        dia_ganador= j+1
        
print(f"El dia con mayores ventas totales fue {dia_ganador} con un total de {suma_dia_ventas} ventas")

print()

print(f"El producto mas vendido en la semana fue el numero {posicion_producto_ganador}")