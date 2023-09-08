precio_por_kilo = input("Ingresa el precio por kilo de las naranjas: ")
peso_bolsa = input("Ingresa el peso de la bolsa de naranjas en kilogramos: ")

precio_por_kilo = float(precio_por_kilo)
peso_bolsa = float(peso_bolsa)
precio_total = precio_por_kilo * peso_bolsa

print("El precio total a pagar por la bolsa: ", precio_total)
