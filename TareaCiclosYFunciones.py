# Tarea 1
def tarea1(n):
    total = 0
    for i in range(n + 1):
        total += i
    return total

# Tarea 2
def tarea2():
    numbers = []
    while True:
        num = int(input("Ingrese un número (0 para finalizar): "))
        if num == 0:
            break
        numbers.append(num)
    average = sum(numbers) / len(numbers)
    return average

# Tarea 3
def tarea3():
    n = int(input("Ingrese la cantidad de artículos: "))
    items = []
    for _ in range(n):
        item = input("Ingrese un artículo: ")
        items.append(item)
    sorted_items = sorted(items)
    return sorted_items

# Tarea 4
def tarea4():
    n = int(input("Ingrese la cantidad de números: "))
    numbers = []
    for _ in range(n):
        num = int(input("Ingrese un número: "))
        if num % 2 == 0:
            numbers.append(num)
    return numbers

# Tarea 5
def tarea5(input_string):
    vowels = "aeiouAEIOU"
    vowel_string = ''.join([char for char in input_string if char in vowels])
    return vowel_string

# Tarea 6
def tarea6(num):
    return num % 243 == 0

# Tarea 7
def multiplicarString(input_string, n):
    return input_string * n

# Tarea 8
def tarea8(a, b, c):
    if a > 100 or b > 100 or c > 100:
        return a + b + c
    else:
        return a * b * c

# Tarea 9
def stringsExclusivos(str1, str2):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    return all(char in vowels for char in str1) and all(char in consonants for char in str2) or \
           all(char in consonants for char in str1) and all(char in vowels for char in str2)

# Tarea 10
def esPalindromo(input_string):
    return input_string == input_string[::-1]

# Tarea 11
def aBinario(number):
    binary_representation = []
    while number > 0:
        binary_representation.insert(0, number % 2)
        number //= 2
    return binary_representation

# Tarea 12
def tarea12(rows):
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

# Ejemplos de uso
n = int(input("Ingrese un número para la tarea 1: "))
print("Tarea 1:", tarea1(n))

print("Tarea 2: El promedio es", tarea2())

print("Tarea 3: Lista de compras ordenada:", tarea3())

print("Tarea 4: Lista de números pares:", tarea4())

input_str = input("Ingrese una cadena para la tarea 5: ")
print("Tarea 5:", tarea5(input_str))

num_for_divisibility = int(input("Ingrese un número para la tarea 6: "))
print("Tarea 6:", tarea6(num_for_divisibility))

string_for_multiplication = input("Ingrese un string para la tarea 7: ")
n_for_multiplication = int(input("Ingrese un número para la tarea 7: "))
print("Tarea 7:", multiplicarString(string_for_multiplication, n_for_multiplication))

a, b, c = map(int, input("Ingrese tres números separados por espacio para la tarea 8: ").split())
print("Tarea 8:", tarea8(a, b, c))

str1_for_exclusive, str2_for_exclusive = input("Ingrese dos strings separados por espacio para la tarea 9: ").split()
print("Tarea 9:", stringsExclusivos(str1_for_exclusive, str2_for_exclusive))

string_for_palindrome = input("Ingrese una cadena para la tarea 10: ")
print("Tarea 10:", esPalindromo(string_for_palindrome))

num_for_binary = int(input("Ingrese un número para la tarea 11: "))
print("Tarea 11:", aBinario(num_for_binary))

rows_for_pyramid = int(input("Ingrese el número de filas para la tarea 12: "))
print("Tarea 12:")
tarea12(rows_for_pyramid)
