eleccion = int(input())

if eleccion == 1:
    #Uno
    def multiplicacion(a, b):
        cont = 0
        total = 0
        while cont != a:
            total += b
            cont += 1
        return total

    num1 = int(input("Ingrese un número entero: "))
    num2 = int(input("Ingrese otro número entero: "))
    
    print("El resultado de multiplicar", num1, "*", num2, "es:", multiplicacion(num1, num2))

if eleccion == 2:
    #Dos
    def potencia(a, b):
        cont = 1
        total = a
        while cont != b:
            total = total*a
            cont += 1
        return total

    num = int(input("Ingrese un número entero: "))
    pot = int(input("Ingrese a que número elevar el número ingresado anteriormente: "))

    print("El resultado de", num, "elevado a la", pot, "es:", potencia(num, pot))

if eleccion == 3:
    #Tres
    def asterisco(y):
        if y>0:
            while y!=0:
                print("*")
                y = y-1
        else:
            print("Error, debe ingresar una altura válida.")

    num = int(input("Ingrese una altura: "))
    asterisco(num)

if eleccion == 4:
    #Cuatro
    def multiplo(a, b):
        multiplo = b%a
        if multiplo == 0:
            res = "es multiplo de"
        else:
            res = "no es multiplo de"
        return res

    n1 = int(input("Ingrese un número entero: "))
    n2 = int(input("Ingrese otro número entero: "))

    print(n1, multiplo(n1, n2), n2)

if eleccion == 5:
    #Cinco
    def signo(n):
        if n>0:
            print(n, "es positivo.")
        elif n<0:
            print(n, "es negativo.")
        else:
            print(n, "es cero.")
    
    num = int(input("Ingrese un número: "))
    res = signo(num)

if eleccion == 6:
    #Seis
    def comparar(a, b):
        if a>b:
            es = 1
        elif a==b:
            es = 0
        else:
            es = -1
        return es
    
    n1 = int(input("Ingrese un numero: "))
    n2 = int(input("Ingrese otro numero: ")) 
    
    print(comparar(n1, n2))

if eleccion == 7:
    #Siete
    def mcd(x, y):
        res = None
        if x>0 and y>0:
            if x>y:
                div = y
                while res!=0:
                    div = div-1
                    if x%div==0 and y%div==0:
                        res=0          
            if x<y:
                div = x
                while res!=0:
                    div = div-1
                    if x%div==0 and y%div==0:
                        res=0
        elif x==0:
            div = y
        elif y==0:
            div = x
        else:
            div = -1
            print("Error, es negativo.")
        return div
    
    n1 = int(input("Ingrese un numero no negativo: "))
    n2 = int(input("Ingrese otro numero no negativo: "))
    
    res = mcd(n1, n2)

    if res!=-1:
        print("El MCD de", n1, "y", n2, "es", res)

if eleccion == 8:
    #Ocho
    def newton(n):
        if n>0:
            a1 = n/2
            a2 = n
            while abs(a1-a2)>0.0001: 
                a2 = a1
                a1 = (n/a1+a1)/2
        else:
            print("Error, debe ingresar un numero positivo.")
            a1 = -1
        return a1
    
    num = int(input("Ingrese un numero: "))
    res = newton(num)

    if res!=-1:
        print(res)

if eleccion == 9:
    pass

if eleccion == 10:
    def extraccion(a, b):
        a = abs(a)
        cont = 0

        while a>0:
            if cont == b:
                return a%10
            a = a // 10
            cont += 1
        return -1
    
    n1 = int(input("Ingrese un número entero: "))
    n2 = int(input("Ingrese posición de dígito a extraer: "))

    print(extraccion(n1, n2))

if eleccion == 11:
    def digcentro(x):
        cont = 0
        n = abs(x)
        while n!=0:
            n = n // 10
            cont += 1
        if cont%2==0:
            return -1
        else:
            cont = int(cont/2)
            n = abs(x)
            while cont!=0:
                n = n // 10
                cont -= 1
            return n%10
    
    num = int(input("Ingrese un número entero: "))

    print(digcentro(num))
