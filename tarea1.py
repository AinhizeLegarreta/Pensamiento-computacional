# 1. Haz un programa que lea 2 números e imprima True si el primero es 20 veces el valor del segundo. Si no, imprime False.
num1 = float(input("Primer número: "))
num2 = float(input("Segundo número: "))

resultado = num1 == 20 * num2
print(resultado)


# 2. Haz un programa que lea tres números e imprima el producto de los tres dividido entre la suma de los tres.
num1 = float(input("Primer número: "))
num2 = float(input("Segundo número: "))
num3 = float(input("Trecer número: "))

resultado = (num1 * num2 * num3) / (num1 + num2 + num3)
print(resultado)


# 3. Haz un programa que lea 3 números e imprima True si están en orden ascendiente. Si no, imprime False.
num1 = float(input("Primer número: "))
num2 = float(input("Segundo número: "))
num3 = float(input("Trecer número: "))

resultado = num1 < num2 < num3
print(resultado)


# 4. Haz un programa lea 4 números e imprima True si todos son negativos. Si alguno es positivo, imprime False.
num1 = float(input("Primer número: "))
num2 = float(input("Segundo número: "))
num3 = float(input("Trecer número: "))
num4 = float(input("Cuarto número: "))

resultado = num1 < 0 and num2 < 0 and num3 < 0 and num4 < 0
print(resultado)


# 5. Haz un programa que lea un número e imprima True si es un número par e imprima False si es un número impar.
num = int(input("Primer número: "))

resultado = num % 2 == 0
print(resultado)


# 6. Haz un programa que lea 3 números e imprima True si el primero es menor que el segundo y si el segundo no es igual al tercero. Si no, imprime false.
num1 = float(input("Primer número: "))
num2 = float(input("Segundo número: "))
num3 = float(input("Trecer número: "))

resultado = num1 < num2 and num2 != num3
print(resultado)


# 7. Haz un programa que lea 3 números e imprima True si el primero y el segundo son iguales o si el primero es al menos 3 unidades más grande que el segundo. Si no, imprime False.
num1 = float(input("Primer número: "))
num2 = float(input("Segundo número: "))
num3 = float(input("Trecer número: "))

resultado = num1 == num2 or num1 - num2 >= 3
print(resultado)


# 8. Haz un programa que lea 8 números e imprima el promedio.
suma = 0
for i in range(8):
    num = float(input("Un número: "))
    suma += num

promedio = suma / 8
print(promedio)


# 9. Haz un programa que lea 4 strings y los concatene.
str1 = input("Primer string: ")
str2 = input("Segundo string: ")
str3 = input("Trecer string: ")
str4 = input("Cuarto string: ")

resultado = str1 + str2 + str3 + str4
print(resultado)


# 10. Sandía (Challenge)
peso = int(input("Peso de la sandía: "))

resultado = peso >= 4 and (peso - 2) % 2 == 0
print(resultado)

