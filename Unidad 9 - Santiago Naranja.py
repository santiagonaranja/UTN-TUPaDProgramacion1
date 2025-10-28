#Ejercicio 1

def fact(x):
    return 1 if x ==0 else x * fact(x - 1)

num= int(input("Ingresar un numero para calcular su factorial: "))

for i in range(1, num + 1):
    print(f"El factorial del numero {i} es {fact(i)}")
    
#Ejercicio 2

def fibonacci(x):
    if x ==0:
        return 0
    elif x == 1:
        return 1
    else: 
        return fibonacci(x-1) + fibonacci(x-2)

num= int(input("Ingresar un numero para mostrar la serie de fibonacci hasta ese valor: "))

for i in range(num + 1):
    print(f"El valor de fibonacci para {i} es {fibonacci(i)}")
    
#Ejercicio 3

def potencia(base, exp):
    
    if exp == 0:
        return 1
    if exp < 0:
        return 1 / potencia(base, -exp)
    
    return base * potencia(base, exp - 1)


def main():
    try:
        base = float(input("Ingresar la base: "))
        exp = int(input("Ingresar el exponente: "))
        resultado = potencia(base, exp)
        print(f"{base} elevado a {exp} = {resultado}")
    except ValueError:
        print("Entrada inválida: la base debe ser número y el exponente un entero.")

if __name__ == "__main__":
    main()

#Ejercicio 4

def decimal_a_binario(decimal):

    if decimal == 0:
        return "0"

    
    def _rec(decimal):
        if decimal == 0:
            return ""
        resto = decimal % 2
        return _rec(decimal // 2) + str(resto)

    return _rec(decimal)


decimal = int(input("Ingresá un número entero positivo: "))
print(f"{decimal} en binario = {decimal_a_binario(decimal)}")

#Ejercicio 5

def es_palindromo(palabra):
    palabra = palabra.lower()

    def _rec(i,j):
        if i >= j:                 
            return True
        if palabra[i] != palabra[j]:
            return False
        return _rec(i + 1, j - 1)  

    return _rec(0, len(palabra) - 1)


print(es_palindromo("neuquen")) 
print(es_palindromo("reconocer")) 
print(es_palindromo("python"))    


#Ejercicio 6

def suma_digitos(n):
    if n < 0:
        raise ValueError("n debe ser un entero positivo")
    if n < 10:                
        return n
    ultimo = n % 10           
    resto = n // 10           
    return ultimo + suma_digitos(resto)

 
print(suma_digitos(12345))

#Ejercicio 7

def contar_bloques(n):
    if n < 0:
        raise ValueError("n debe ser un entero")
    if n == 0:        
        return 0
    if n == 1:       
        return 1
    return n + contar_bloques(n - 1)



print(contar_bloques(1))  
print(contar_bloques(2))  
print(contar_bloques(4))  

#Ejercicio 8

def contar_digito(numero,digito):
    if numero < 0:
        raise ValueError("numero debe ser un entero")
    if not (isinstance(digito, int) and 0 <= digito <= 9):
        raise ValueError("digito debe ser un entero entre 0 y 9")

    if numero == 0:
        return 1 if digito == 0 else 0

    def _rec(n):
        if n == 0:
            return 0
        ultimo = n % 10
        cuenta_actual = 1 if ultimo == digito else 0
        return cuenta_actual + _rec(n // 10)

    return _rec(numero)



print(contar_digito(12233421, 2))  
print(contar_digito(5555, 5))      
print(contar_digito(123456, 7))    

