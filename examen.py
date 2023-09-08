############## EXAMEN ##############

######### Práctica #########
# Tarea 1
corriente = int(input("Ingresa la corriente: "))
resistencia = int(input("Ingresa la resistencia: "))
voltaje = corriente * resistencia
print("Este es el voltaje del circuito electrico: " + str(voltaje))


# Tarea 2
print("El precio de los vuelos hoy es 8,000 MNX")
precio_pasado = int(input("Ingresa el precio del año pasado: "))
diferencia = 8000 - precio_pasado
porcentaje_incremento = diferencia*100/precio_pasado
print("La diferencia en precio es de " + str(diferencia))
print("El porcentaje de incremento es de " + str(porcentaje_incremento) + "%")


# Tarea 3
numero = int(input("Ingresa un número entero cualquiera: "))
par = "impar"
if (numero%2 == 0):
    par = "par"
print(str(numero)+ " es un número " + par + ".")
    


# Tarea 4
libros = ["Biblia", "Corán", "Principito", "El diario de Greg", "Programación en Python", "Algoritmos avanzados", "Algebra de Baldor"]
print("La lista de libros: " + str(libros))
for i in range(4):
    libro = input("Introduce el nombre de un libro para agregar: ")
    if libro in libros:
        print("Ya existe en la lista")
        
    else:
        libros.append(libro)
print("La lista de libros actualizada: " + str(libros))

for i in range(2):      
    libro = input("Introduce el nombre del libro para eliminar: ")
    if libro in libros:
        libros.remove(libro)
    else:
        print("No existe en la lista")
print("La lista de libros actualizada: " + str(libros))

for i in range(2): 
    print("Introduce el nombre de los libros para cambiar de lugar. ")   
    libro1 = input("Libro 1: ")
    libro2 = input("Libro 2: ")
    if (libro1 in libros) and (libro2 in libros):
        ###########libros.pop(libro)
        a, b = libros.index(libro1), libros.index(libro2)
        libros[b], libros[a] = libros[a], libros[b]
    else:
        print("No existe alguno de los libros")
print("La lista de libros actualizada: " + str(libros))


# Tarea 5
num_lados = int(input("Ingresa 5 si es pentagonal y 6 si es hexagonal: "))
lado = int(input("Ingresa el valor de un lado: "))
apotema = int(input("Ingresa el valor del apotema: "))
perimetro = num_lados*lado

area = perimetro*apotema/2
print("El area es de " + str(area) + ".")



######### Teoría #########
# Tarea 6
# append, pop

# Tarea 7
# len

# Tarea 8
# Es una seguida de carácteres, ya sean numéricos o letras; pero si son números,
# el programa no los leerá como tal y por lo tanto se tendrá que parsear.

# Tarea 10
# Las variables de Python son ubicaciones de memoria reservadas para almacenar valores. 
# Pueden ser caracter, string, int... al que se le puede asignar diferentes valores cómo números, letras... 
# y la cual puede variar durente la ejecución dependiendo de los comandos que utilicemos

# Tarea 11
# and >> se deben cumplir las dos condiciones
# or >> se deben cumplir alguna de las dos condiciones
# and >> no se debe de cumplir la condición



######### Challenges #########
# Tarea 12
import math
lado = int(input("Ingresa el lado del triángulo: "))
area = math.sqrt(3)/4*(lado**2)
print("El area es de " + str(area) + ".")


# Tarea 13
texto = input("Ingresa un texto cualquiera: ")
if len(texto)>500:
    print("Error!! El texto tiene más de 500 caracteres")