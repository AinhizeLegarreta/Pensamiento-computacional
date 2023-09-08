# 1. Escribe un programa que le pida al usuario que introduzca un mes.
    # El programa debe imprimir cuantos días hay en ese mes

meses = {
        "enero": 31,
        "febrero": 28,
        "marzo": 31,
        "abril": 30,
        "mayo": 31,
        "junio": 30,
        "julio": 31,
        "agosto": 31,
        "septiembre": 30,
        "octubre": 31,
        "noviembre": 30,
        "diciembre": 31
    }
    
mes_elegido = input("Introduce un mes: ").lower()

if mes_elegido in meses:
    dias = meses[mes_elegido]
    print("El mes de " + mes_elegido + " tiene " + str(dias) + " días.")
else:
    print("Mes no válido.")






# 2. Escribe un programa que le pida al usuario que introduzca un día de la semana
    #. El programa debe imprimir la posición de ese día en la semana.

dias = {
        "lunes": 1,
        "martes": 2,
        "miercoles": 3,
        "jueves": 4,
        "viernes": 5,
        "sabado": 6,
        "domingo": 7,
}

dia_elegido = input("Introduce un día de la semana: ").lower()

if dia_elegido in dias:
    numero = dias[dia_elegido]
    print("El día de " + dia_elegido + " tiene como número el " + str(numero) + ".")
else:
    print("Mes no válido.")






# 3. Escribe un programa que le pida al usuario un año e imprima “Bisiesto”/“No bisiesto”.

año = int(input("Introduce un año: "))

if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print(str(año) +" es un año bisiesto.")
else:
    print(str(año) +" no es un año bisiesto.")
    
    
    
    
    
# 4. Pide al usuario que ingrese un número entero cualquiera. 
    # Indica si es positivo o no, si es un número par, si es menor o mayor que 100. 

numero = int(input("Ingresa un número entero cualquiera: "))
positivo = "positivo"
par = "impar"
menor_100 = "menor"

if (numero < 0):
    positivo = "negativo"
if (numero%2 == 0):
    par = "par"
if (numero > 100):
    menor_100 = "mayor"
print(str(numero)+ ": es un número " + positivo + ", " + par + " y " + menor_100 + " que 100.")





# 5. Dado el siguiente arreglo = [‘Do’, ‘Re’, ‘Mi’, ‘Fa’, ‘Sol’, ‘La’, ‘Si’] y accediendo a él.
    # Imprime lo siguiente: Si Si Do Re Re Do Si La Sol Sol La Si Si La La
    
dias = {
        "Do": 1,
        "Re": 2,
        "Mi": 3,
        "Fa": 4,
        "Sol": 5,
        "La": 6,
        "Si": 7,
}

print("Aquí va una canción: ")




# 7. Dado el siguiente arreglo = [ “Jose Miguel”, “Carlos”, “Manuel”, “Memo” ]
    # reciba un string del usuario e indique si ese string aparece dentro del arreglo o no

arreglo = ["Jose Miguel", "Carlos", "Manuel", "Memo"]
elemento = input("Introduce un nombre: ")

if elemento in arreglo:
    print("True")
else:
    print("False")





# 8. Dado el siguiente arreglo = [12,456,2,123], ordenalo e imprimelo siendo [2,12,123,456].

arreglo = [12, 456, 2, 123]
arreglo.sort()
print("[12, 456, 2, 123] arreglo ordenado:")
print(arreglo)





# 9. Crea un programa que lea 6 números del teclado y los guarde en un arreglo.
    # Luego imprime la resta de la suma de los índices pares con la suma de los índices impares.
    
numeros = []
for i in range(6):
    numero = int(input("Introduce un número: "))
    numeros.append(numero)

suma_indices_pares = sum(numeros[::2]) # Suma de los índices pares
suma_indices_impares = sum(numeros[1::2]) # Suma de los índices impares

resultado = suma_indices_pares - suma_indices_impares
print("La resta de la suma de los índices pares con la suma de los índices impares es:", resultado)






# 10. Challenge: dado un arreglo con cinco elementos ingresados por el usuario
    # imprimir “Es palíndromo” si el arreglo es palíndromo o “No palíndromo” si no
    
numeros = []
for i in range(5):
    numero = int(input("Introduce un número: "))
    numeros.append(numero)

es_palindromo = True
for i in range(len(arreglo) // 2):
    if arreglo[i] != arreglo[-i - 1]:
        es_palindromo = False
        break

if es_palindromo:
    print("Es palíndromo")
else:
    print("No es palíndromo")
    





# 11. Challenge: Averigua si es un cuadrado
    # Vas a recibir dos números decimales: lado y diagonal de un

import math

lado = float(input("Introduce la longitud del lado: "))
diagonal = float(input("Introduce la longitud de la diagonal: "))

diagonal_esperada_cuadrado = lado * math.sqrt(2)

if diagonal == diagonal_esperada_cuadrado:
    print("Es un cuadrado")
else:
    print("No es un cuadrado")
