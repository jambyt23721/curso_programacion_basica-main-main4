lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]
comunes = []

for elemento in lista1:
    if elemento in lista2 and elemento not in comunes:
        comunes.append(elemento)
        print(comunes)