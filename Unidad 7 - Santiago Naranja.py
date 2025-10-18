#Ejercicio 1

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300

print(precios_frutas)

#Ejercicio 2

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800

print(precios_frutas)

#Ejercicio 3

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800

frutas = list(precios_frutas.keys())

print(frutas)

#Ejercicio 4

numeros_telefonicos= {}
for i in range(5):
    nombre = input(f"Escribir el nombre del contacto {i+1}: ").strip()
    numero = input(f"Escribir el número del contacto {i+1}: ").strip()
    numeros_telefonicos[nombre] = numero

nombre_consulta=input(f"El numero de que nombre queres consultar?: ").strip()

numero = numeros_telefonicos.get(nombre_consulta)

if numero is None:
    print("Ese contacto no existe.")
else:
    print(f"El número de {nombre_consulta} es {numero}.")
    


#Ejercicio 5


frase= input("Ingresá una frase: ").strip().lower()

palabras = frase.split()           
unicas = set(palabras)             
conteos = {}                       

for p in palabras:
    conteos[p] = conteos.get(p, 0) + 1

print("Palabras únicas:", unicas)
print("Conteos:", conteos)


#Ejercicio 6


alumnos= {}
for i in range(3):
    nombre = input(f"Escribir el nombre del alumno {i+1}: ").strip()
    
    notas=[]
    for t in range(3):
        n = int(input(f"Escribir la nota numero {t+1}: ").strip())
        notas.append(n)
        
    alumnos[nombre] = tuple(notas)

print(alumnos)

#ejercicio 7

primer_parcial = {"Santiago", "Jose", "Manuel", "Maria"}
segundo_parcial = {"Santiago", "Jose", "Tobias", "Pedro"}


ambos_parciales = primer_parcial & segundo_parcial         


solo_un_parcial = primer_parcial ^ segundo_parcial          


al_menos_uno = primer_parcial | segundo_parcial             

print("Ambos:", ambos_parciales)
print("Solo uno:", solo_un_parcial)
print("Al menos uno:", al_menos_uno)

#ejercicio 8

productos_stock = {'pantalon': 1200, 'remera': 2500, 'cinturon': 3000, 'gorras': 1450}

print(f"Estos son los productos que tenemos {productos_stock.keys()}")
consulta_stock= input("Que producto queres ver el stock?: ").strip().lower()
        

if consulta_stock in productos_stock:
    agregar_stock=int(input("Cuanto stock queres agregar?: "))
    productos_stock[consulta_stock]+=agregar_stock    
    
if consulta_stock not in productos_stock:
    agregar_stock=int(input("Agregar el stock del nuevo producto: "))
    productos_stock[consulta_stock]=agregar_stock
    
print(productos_stock)

#Ejercicio 9

agenda = {
    ("lunes", "10:00"): "Reunión",
    ("martes", "15:00"): "Clase de ingles",
    ("lunes", "11:00"): "Gym",
    
}

dia=input("Ingresar dia a consultar: ").strip().lower()
hora=input("Ingresar horario a consultar en formato 10:00 : ").strip().lower()

print(f"La actividad que hay el {dia} en el horario {hora} es: {agenda[(dia,hora)]}")

#Ejercicio 10

original = {"Argentina": "Buenos Aires", "Chile": "Santiago"}

invertido = {}                 
for pais in original:          
    ciudad_aux = original[pais]  
    invertido[ciudad_aux] = pais 
    
print(invertido)