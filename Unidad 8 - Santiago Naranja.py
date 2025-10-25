#Ejercicio 1

with open("productos.txt", "w") as archivo:
    archivo.writelines("Nombre,Precio,Cantidad\n")
    archivo.writelines("Heladera,500000,50\n")
    archivo.writelines("Mesa,10000,100\n")
    archivo.writelines("Vaso,500,80\n")
    
    
#Ejercicio 2

with open("productos.txt", "r") as archivo:
    next(archivo)
    for linea in archivo:
        linea = linea.strip()
        partes = linea.split(",")
        print(f"Producto: {partes[0]} | Precio: ${partes[1]} | Cantidad: {partes[2]}")
        
#Ejercicio 3

with open("productos.txt", "r") as archivo:
    next(archivo)
    for linea in archivo:
        linea = linea.strip()
        partes = linea.split(",")
        print(f"Producto: {partes[0]} | Precio: ${partes[1]} | Cantidad: {partes[2]}")
        
with open("productos.txt", "a") as archivo:
    producto=input("Agregar un nuevo producto: ").strip()
    precio=input("Agregar el precio de ese producto: ").strip()
    cantidad=input("Agregar la cantidad de ese producto: ").strip()
    archivo.write(f"{producto},{precio},{cantidad}\n")


#Ejercicio 4
lista=[]
with open("productos.txt", "r") as archivo:
    next(archivo)
    for linea in archivo:
        linea = linea.strip()
        partes = linea.split(",")
        lista.append({"Producto": partes[0], "Precio": partes[1], "Cantidad": partes[2]})
 
print(lista)


#Ejercicio 5
lista=[]
with open("productos.txt", "r") as archivo:
    next(archivo)
    for linea in archivo:
        linea = linea.strip()
        partes = linea.split(",")
        lista.append({"Producto": partes[0], "Precio": partes[1], "Cantidad": partes[2]})
 
consulta=input("Ingresar un producto que queres buscar: ").strip()

encontrado= False
for productos in lista:
    if productos["Producto"] == consulta:
        print(f"Producto: {productos["Producto"]} | Precio: ${productos["Precio"]} | Cantidad: {productos["Cantidad"]}")
        encontrado=True
        break
        
if not encontrado:        
    print("No se encontro el producto")
        
        
#Ejercicio 6
lista=[]
with open("productos.txt", "r") as archivo:
    next(archivo)
    for linea in archivo:
        linea = linea.strip()
        partes = linea.split(",")
        lista.append({"Producto": partes[0], "Precio": partes[1], "Cantidad": partes[2]})
 
consulta=input("Ingresar un producto que queres buscar: ").strip()

encontrado= False
for productos in lista:
    if productos["Producto"] == consulta:
        print(f"Producto: {productos["Producto"]} | Precio: ${productos["Precio"]} | Cantidad: {productos["Cantidad"]}")
        encontrado=True
        break
        
if not encontrado:        
    print("No se encontro el producto")
        
with open("productos.txt", "w") as archivo:
    archivo.write("Nombre,Precio,Cantidad\n")
    for carga in lista:
        archivo.write(f"{carga['Producto']},{carga['Precio']},{carga['Cantidad']}\n")
        