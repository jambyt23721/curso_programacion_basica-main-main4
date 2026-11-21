numeros = []

print("Ingrese los numeros 1x1 para calcular su promedio:")
print("Escribe 'Fin' cuando quieras acabar")

print()

while True:
    entrada = input("Ingresa un numero")
    if entrada.lower() == "fin":
        break
    numero = float(entrada)
    numeros.append(numero)
print()

if len(numeros) > 0:
    promedio = len(numeros)
    print(f"Numeros ingresados: {numeros}")
    print(f"El promedio es: {promedio:.2f}")
else:
    print("No ingresaste ningun numero")