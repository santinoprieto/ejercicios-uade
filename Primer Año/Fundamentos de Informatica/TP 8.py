import random
eleccion = int(input("Seleccione ejercicio: "))

if eleccion == 1:
    matriz = [[0, 0, 0, 0], 
              [0, 0, 0, 0], 
              [0, 0, 0, 0]]

    for c in range(len(matriz)):
        for f in range(len(matriz)+1):
            numero = random.randint(1, 10)
            matriz[c][f] = numero

    print(matriz)

if eleccion == 2:
    matriz = []
    n = int(input("numero: "))
    
    for i in range(n):
        lista = []
        for j in range(n):
            numero = random.randint(1, 10)
            lista.append(numero)
        matriz.append(lista)
    
    print(matriz)

if eleccion == 3:
    matriz = []

    m = int(input("Filas: "))
    n = int(input("Columnas: "))
    a = int(input("Rango 1: "))
    b = int(input("Rango 2: "))

    for i in range(m):
        lista = []
        for j in range(n):
            numero = random.randint(a, b)
            lista.append(numero)
        matriz.append(lista)
    
    print(matriz)

if eleccion == 4:
    matriz = []

    m = int(input("Filas: "))
    n = int(input("Columnas: "))

    mayor = 0
    coordenadas = [0, 0]

    for i in range(m):
        lista = []
        for j in range(n):
            numero = random.randint(100, 1000)
            lista.append(numero)
            if numero > mayor:
                mayor = numero
                coordenadas[0] = i
                coordenadas[1] = j
        matriz.append(lista)
    
    print(matriz)
    print(coordenadas)