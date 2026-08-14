#Funcion para demas ejercicios
import random
def crearlista():
    n= int(input("Ingrese un número o -99 para terminar: "))
    lista = []
    while n!=-99:
        lista.append(n)
        n=int(input("Ingrese un número o -99 para terminar: "))
    return lista

def secuencial(a):
        largo = len(a)
        for i in range(largo-1):
            for j in range(i+1, largo):
                if a[i] > a[j]:
                    aux = a[i]
                    a[i] = a[j]
                    a[j] = aux
        return a

def busquedabinaria(lista, dato):
    izq = 0
    der = len(lista) - 1
    pos = -1
    while izq <= der and pos == -1:
        centro = (izq + der) // 2
        if lista[centro] == dato:
            pos = centro
        elif lista[centro] < dato:
            izq = centro + 1
        else:
            der = centro - 1
    return pos

def cargar_listas(n):
    lista = []

    for i in range(n):
        lista.append(random.randint(1, 100))
    return lista

def rango(a, b):
        if a<=b:
            c = a
            numeros = []
            n = int(input("Ingrese un número o -1 para terminar: "))
            while n!=-1:
                if n>=a and n<=b:
                    numeros.append(c)
                    c += 1
                else:
                    print("Valor ya añadido o fuera del rango.")
                n = int(input("Ingrese un número o -1 para terminar: "))
        else:
            numeros = "A debe ser el valor menor del rango, B no puede ser menor."
        return numeros

#Programa principal
eleccion = int(input("Ingrese número entre 1 y 5: "))

if eleccion == 1:
    #Uno
    n1 = int(input("Ingrese un valor de A: "))
    n2 = int(input("Ingrese un valor de B: "))
    print(rango(n1, n2))

if eleccion == 2:
    #Dos
    n1 = int(input("Ingrese un valor de A: "))
    n2 = int(input("Ingrese un valor de B: "))

    numeros = rango(n1, n2)
    total = 0

    for i in range(len(numeros)):
        total += numeros[i]
    print(total)

if eleccion == 3:
    #Tres
    lista = []
    n = int(input("Ingrese un número o -1 para terminar: "))

    while n!= -1:
        lista.append(n)
        n = int(input("Ingrese un número o -1 para terminar: "))
    
    cant = len(lista)//2
    list1 = []
    list2 = []

    for i in range(cant+1):
        list1.append(lista[i])
        list2.append(lista[(i*-1)-1])

    if list1 == list2:
        print("Es capicua.")
    elif list1 != list2:
        print("No es capicua.")

if eleccion == 4:
    #Cuatro
    def conteo(a, b):
        total = []
        for i in range(len(a)):
            if a[i] == b:
                total.append(i)
        return total
    
    cantidad = int(input("Ingrese cantidad de números para la lista: "))
    lista = []
    
    for i in range(cantidad):
        num = int(input("Ingrese un número:"))
        lista.append(num)
    
    n = int(input("Ingrese número a encontrar en la lista: "))

    print(conteo(lista, n))

if eleccion == 5:
    #Cinco
    def invertido(a):
        lista = []
        for i in range(len(a)):
            lista.append(a[i*-1-1])
        return lista
    
    numeros = [1, 2, 3, 4]

    print(invertido(numeros))

if eleccion == 6:    
    def posiciones(x, lista):
        l_posiciones = []
        for i in range(len(lista)):
            if lista[i] == x:
                l_posiciones.append(i)
        return l_posiciones

    lista_input = crearlista()
    num = int(input("Ingrese número a buscar: "))
    print(posiciones(num, lista_input))

if eleccion == 7:
    lista_input = crearlista()
    num = int(input("Ingrese número a buscar: "))

    lista_ordenada = secuencial(lista_input)
    print(busquedabinaria(lista_ordenada, num))

if eleccion == 8:
    def listarandom(lista):
        numero = random.randint(0, 100)
        while numero!=0:
            lista.append(numero)
            numero = random.randint(0, 100)
        return lista
    
    def posicion(lista):
        posiciones = [0]
        for i in range(len(lista)):
            for j in range(i+1, len(lista)):
                if lista[0] == lista[j]:
                    posiciones.append(j)
        return posiciones

    def minimo(lista):
        valor = []
        valor.append(lista[0])
        for i in range(len(lista)):
            for j in range(i+1, len(lista)):
                if lista[0] == lista[j]:
                    valor.append(lista[j])
        return valor

    lista_input = []

    print("lista random:" , listarandom(lista_input) , "\n")
    print("ordenada:" , secuencial(lista_input) , "\n")
    print("valor/es mínimo/s:" , minimo(lista_input) , "\n")
    print("posiciones:" , posicion(lista_input))

if eleccion == 9:
    def azarlista1(n):
        lista = []
        if n > 101:
            n = 101

        while len(lista) < n:
            num = random.randint(0, 100)
            if num not in lista:
                lista.append(num)
        return lista

    def azarlista2(n):
        lista = []
        if n > 101:
            n = 101

        for i in range(n):
            num = random.randint(0, 100)
            lista.append(num)

        for i in lista:
            for j in range(len(lista)-1, -1, -1):
                if i == lista[j]:
                    del lista[j]
        return lista
    
# En la 2 no pude hacer que sea la cantidad N la lista

    veces = int(input("Ingrese cantidad de numeros de la lista: "))

    print("La forma 1:" , azarlista1(veces) , "\n")
    print("La forma 2:" , azarlista2(veces))

if eleccion == 10:
    def eliminar(numeros, borrar):
        lnueva = []
        
        for num in numeros:
            lnueva.append(num)
        
        for i in borrar:
            for j in range(len(lnueva)-1, -1, -1):
                if i == lnueva[j]:
                    del lnueva[j]
        return lnueva

    def listavalor():
        lista = []
        
        for i in range(random.randint(4, 20)):
            lista.append(random.randint(0, 10))
        
        return lista
    
    lista_comun = listavalor()
    lista_borrar = listavalor()

    print("Lista:", lista_comun, "\n")
    print("A borrar:", lista_borrar, "\n")

    resultado = eliminar(lista_comun, lista_borrar)

    print("Resultado:", resultado)

if eleccion == 11:
    def lista_c(a, b):
        c = []
        
        for i in a:
            if i%2 == 0:
                c.append(i)
        
        for i in b:
            if i%2 != 0:
                c.append(i)
        return c
    
    def lista_d(a, b):
        d = []

        for i in a:
            if i%2 != 0:
                d.append(i)
        
        reverso = []
        for i in b:
            if i%2 == 0:
                reverso.append(i)
        
        for i in range(len(reverso)-1, -1, -1):
            d.append(reverso[i])

        return d
    
    def lista_e(a, b, n):
        e = []
        largo = len(a) + len(b)

        for i in range(n):
            e.append(a[i])
            e.append(b[i])
        return e
    
    cantidad = int(input("Ingrese la cantidad de elementos de las listas: "))

    lista_a = cargar_listas(cantidad)
    lista_b = cargar_listas(cantidad)

    conca_apar_bimp = lista_c(lista_a, lista_b)
    conca_aimp_bpar = lista_d(lista_a, lista_b)
    inter = lista_e(lista_a, lista_b, cantidad)

    print("Lista A:", lista_a, 
          "\nLista B:", lista_b, 
          "\nLista C(par de A + impar de B):", conca_apar_bimp, 
          "\nLista D(impar de A + reverso de par de B):", conca_aimp_bpar, 
          "\nLista E(intercalacion de A y B):", inter)

if eleccion == 12:
    def clasificacion(a):
        for i in range(len(a)-1):
            if a[i] < a[i+1]:
                return True
            elif a[i] > a[i+1]:
                return False

    def agregado(a, n, x):
        a.append(n)
        largo = -len(a)
        indice = -1

        for i in range(-2, largo, -1):
            if x == True and a[indice] < a[i]:
                aux = a[i]
                a[i] = a[indice]
                a[indice] = aux
                indice = indice-1
            elif x == False and a[indice] > a[i]:
                aux = a[i]
                a[i] = a[indice]
                a[indice] = aux
                indice = indice-1

        return a
    
    lista = [12, 11, 10, 7, 6, 4, 1]
    num = 8
    
    menoramayor = clasificacion(lista)

    print(agregado(lista, num, menoramayor))

if eleccion == 13:
    def intercalar(m, n):
        c = []
        largo = len(m) + len(n)
        indice = 0

        for i in m:
            if i < n[indice]:
                c.append(i)
            elif n[indice] < i:
                c.append(n[indice])
            indice = indice + 1
        return c
    
    cantidad = int(input("Tamaño de listas: "))

    lista_m = cargar_listas(cantidad)
    lista_n = cargar_listas(cantidad)

    print("\ndesordenado:", lista_m, lista_n, "\n")

    secuencial(lista_m)
    secuencial(lista_n)

    print("ordenadas:", lista_m, lista_n, "\n")

    print("intercalado en orden:", intercalar(lista_m, lista_n), "\n")

if eleccion ==  14:
    def verificacion(d, m, a):
        if m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
            if d<1 or d>31:
                return False
            else:
                return True
        elif m==4 or m==6 or m==9 or m==11:
            if d<1 or d>30:
                return False
            else:
                return True
        elif m==2:
            if (a%4==0 and a%100!=0) or (a%4==0 and a%100==0 and a%400==0):
                if d<1 or d>29:
                    return False
            else:
                if d<1 or d>28:
                    return False
                else:
                    return True
        elif m<1 or m>12:
            return False
        else:
            return True

    def listacumple(l, n):
        input_l = int(input("Ingrese número de legajo o -1 para terminar: "))
        
        mes_mayor = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] #Indice 0 no cuenta

        while input_l != -1:
            input_d = int(input("día: "))
            input_m = int(input("mes: "))
            input_a = int(input("año: "))
            
            correcto = verificacion(input_d, input_m, input_a)

            if correcto == False:
                print("Error, dió una fecha incorrecta, vuelva a ingresar todo nuevamente.")
            elif correcto == True:
                mes_mayor[input_m] += 1
                agregado = str(input_d) + "/" + str(input_m) + "/" + str(input_a)
                l.append(input_l)
                n.append(agregado)
            
            input_l = int(input("Ingrese número de legajo o -1 para terminar: "))
        
        mayor = 0
        n_mes = 0
        for i in range(1, 13):
            if mes_mayor[i] > mayor:
                mayor = mes_mayor[i]
                n_mes = i

        return n_mes
    
    dia = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]

    mes = ["Ninguno", "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

    año = [2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]

    legajo = []
    nacimiento = []

    mes_cumpleaños = listacumple(legajo, nacimiento)

    print("\nLegajos: ", legajo, "\n")
    print("Nacimientos: ", nacimiento, "\n")
    print("Mes con mayor cantidad de cumpleaños:", mes[mes_cumpleaños], "\n")