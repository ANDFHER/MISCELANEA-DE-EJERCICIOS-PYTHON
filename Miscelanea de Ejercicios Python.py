import math

print("MISCELANEA DE EJERCICIOS PYTHON")


Menuprincipal = int(input("Menu: \n 1-Operadores \n 2-Condicionales \n 3-Ciclos \n 99-Salir del Programa \n "))
while Menuprincipal != 99:
    if Menuprincipal ==1:

        print("Operadores")
        Operadores = int(input("1-Calcular area de un triangulo \n 2-Suma de dos numeros ingresados \n 3-ingesa un numero y visualizarlo al cuadrado \n 4-Algoritmo de Euros a Dolares \n 5-Area y Perimetro de un Cuadrado \n 6-Area y Volumen de un Cilindro \n 7-Segun el Rdio Hallar Circunferencia Longitud y Area de un Circulo \n 8-Calcular el promedio de tres Numeros \n 9-Volver al menu anterior \n"))
        while Operadores !=9:

            if Operadores ==1:
                print("Calcular area de un triangulo")

                base = int(input("Ingrese el Valor de Base"))
                altura = int(input("Ingrese el Valor de Altura"))
                Area = base*altura/2

                print("El area del triangulo es : " + str(round(Area, 1)))

                Operadores = int(input("1-Calcular area de un triangulo \n 2-Suma de dos numeros ingresados \n 3-ingesa un numero y visualizarlo al cuadrado \n 4-Algoritmo de Euros a Dolares \n 5-Area y Perimetro de un Cuadrado \n 6-Area y Volumen de un Cilindro \n 7-Segun el Rdio Hallar Circunferencia Longitud y Area de un Circulo \n 8-Calcular el promedio de tres Numeros \n 9-Volver al menu anterior \n"))

            elif Operadores ==2:
                print("Suma de dos numeros ingresados")

                Num1 = int(input("Ingrese el Primer numero: "))
                Num2 = int(input("Ingrese el Segundo numero: "))
                Suma = Num1 + Num2
                print("El resultado de la suma es: ", Suma)

                Operadores=int(input("1-Calcular area de un triangulo \n 2-Suma de dos numeros ingresados \n 3-ingesa un numero y visualizarlo al cuadrado \n 4-Algoritmo de Euros a Dolares \n 5-Area y Perimetro de un Cuadrado \n 6-Area y Volumen de un Cilindro \n 7-Segun el Rdio Hallar Circunferencia Longitud y Area de un Circulo \n 8-Calcular el promedio de tres Numeros \n 9-Volver al menu anterior \n"))

            elif Operadores ==3:
                print("ingesa un numero y visualizarlo al cuadrado")

                Numero = int(input("ingrese numero: "))
                Potencia = Numero ** 2
                print("El resultado elevado al cuadrado es: " + str(round(Potencia, 1)))

                Operadores=int(input("1-Calcular area de un triangulo \n 2-Suma de dos numeros ingresados \n 3-ingesa un numero y visualizarlo al cuadrado \n 4-Algoritmo de Euros a Dolares \n 5-Area y Perimetro de un Cuadrado \n 6-Area y Volumen de un Cilindro \n 7-Segun el Rdio Hallar Circunferencia Longitud y Area de un Circulo \n 8-Calcular el promedio de tres Numeros \n 9-Volver al menu anterior \n"))

            elif Operadores == 4:
                print("Algoritmo de Euros a Dolares")

                Euro = float(input("Ingrese la cantidad en Euros: "))
                Dollar = Euro * 1.09
                print("equivale en Dolares $" + str(round(Dollar, 2)))

                Operadores=int(input("1-Calcular area de un triangulo \n 2-Suma de dos numeros ingresados \n 3-ingesa un numero y visualizarlo al cuadrado \n 4-Algoritmo de Euros a Dolares \n 5-Area y Perimetro de un Cuadrado \n 6-Area y Volumen de un Cilindro \n 7-Segun el Rdio Hallar Circunferencia Longitud y Area de un Circulo \n 8-Calcular el promedio de tres Numeros \n 9-Volver al menu anterior \n"))

            elif Operadores ==5:
                print("Area y Perimetro de un Cuadrado")

                Lado = float(input("Ingrese el lado de un cuadrado: "))

                Area = Lado ** 2
                Perimetro = Lado * 4

                print("El area del cuadrado es: " + str(round(Area, 2)))
                print("El Perimetro del cuadrado es: " + str(round(Perimetro, 2)))

                Operadores=int(input("1-Calcular area de un triangulo \n 2-Suma de dos numeros ingresados \n 3-ingesa un numero y visualizarlo al cuadrado \n 4-Algoritmo de Euros a Dolares \n 5-Area y Perimetro de un Cuadrado \n 6-Area y Volumen de un Cilindro \n 7-Segun el Rdio Hallar Circunferencia Longitud y Area de un Circulo \n 8-Calcular el promedio de tres Numeros \n 9-Volver al menu anterior \n"))

            elif Operadores ==6:
                print("Area y volumen de un cilindro")

                Radio = float(input("ingrese el radio en Cm: "))
                Altura = float(input("ingrese la altura en Cm: "))

                Area = 2 * math.pi * Radio * Altura
                Volumen = math.pi * Radio ** 2 * Altura

                print("el Area del cilindro es: " + str(round(Area, 2)))
                print("el Volumen del cilindro es: " + str(round(Volumen, 2)))

                Operadores=int(input("1-Calcular area de un triangulo \n 2-Suma de dos numeros ingresados \n 3-ingesa un numero y visualizarlo al cuadrado \n 4-Algoritmo de Euros a Dolares \n 5-Area y Perimetro de un Cuadrado \n 6-Area y Volumen de un Cilindro \n 7-Segun el Rdio Hallar Circunferencia Longitud y Area de un Circulo \n 8-Calcular el promedio de tres Numeros \n 9-Volver al menu anterior \n"))

            elif Operadores ==7:
                print("Hallar Longitud y area de un circulo")

                Radio = float(input("ingrese el radio del circulo en Cm:  "))
                Longitud = 2 * math.pi * Radio
                Area = math.pi * Radio ** 2

                print(f"El Area es:    {Area:.2f}")
                print(f"La Longitud es:    {Longitud:.2f}")

                Operadores=int(input("1-Calcular area de un triangulo \n 2-Suma de dos numeros ingresados \n 3-ingesa un numero y visualizarlo al cuadrado \n 4-Algoritmo de Euros a Dolares \n 5-Area y Perimetro de un Cuadrado \n 6-Area y Volumen de un Cilindro \n 7-Segun el Rdio Hallar Circunferencia Longitud y Area de un Circulo \n 8-Calcular el promedio de tres Numeros \n 9-Volver al menu anterior \n"))

            elif Operadores==8:
                print("calcular el promedio de 3 numeros ingresados")

                n1 = int(input("ingrese el primer numero :"))
                n2 = int(input("ingrese el segundo numero :"))
                n3 = int(input("ingrese el tercer numero :"))

                Suma = n1 + n2 + n3
                Promedio = Suma / 3
                print("el promedio es: ", Promedio)

                Operadores=int(input("1-Calcular area de un triangulo \n 2-Suma de dos numeros ingresados \n 3-ingesa un numero y visualizarlo al cuadrado \n 4-Algoritmo de Euros a Dolares \n 5-Area y Perimetro de un Cuadrado \n 6-Area y Volumen de un Cilindro \n 7-Segun el Rdio Hallar Circunferencia Longitud y Area de un Circulo \n 8-Calcular el promedio de tres Numeros \n 9-Volver al menu anterior \n"))

            else:
                print("Por Favor Digite Una Opcion Correcta")
                Operadores=int(input("1-Calcular area de un triangulo \n 2-Suma de dos numeros ingresados \n 3-ingesa un numero y visualizarlo al cuadrado \n 4-Algoritmo de Euros a Dolares \n 5-Area y Perimetro de un Cuadrado \n 6-Area y Volumen de un Cilindro \n 7-Segun el Rdio Hallar Circunferencia Longitud y Area de un Circulo \n 8-Calcular el promedio de tres Numeros \n 9-Volver al menu anterior \n"))

    elif Menuprincipal ==2:
        print("Condicionales")
        Condicionales = int(input("1-Identificar si el numero es Positivo o Negativo \n 2-indicar cual de los dos numeros es mayor y cual menor \n 3-indicar de los tres numeros cual es el mayor y cual el menor \n 4-nuemros A y B, si A es Menor que B sumarlos de lo contrario restar. \n 5-encontrar el cociente entre A y B, Si la division es por cero indicar que no es posible \n 6- Dos numeros A y B, sumarlos si uno de los dos es negativo, de lo contrario multiplicar \n 7-dar un algoritmo que indique si el año es biciesto o no \n 8-Volver al menu anterior \n"))
        while Condicionales != 8:

            if Condicionales == 1:
                print("Identificar si el numero es Positivo o Negativo")

                n = int(input("ingresa un numero entero: "))
                if n >= 0:
                    print("El numero ", n, " es Positivo")
                else:
                    print("El numero ", n, " es Negativo")
                Condicionales = int(input("1-Identificar si el numero es Positivo o Negativo \n 2-indicar cual de los dos numeros es mayor y cual menor \n 3-indicar de los tres numeros cual es el mayor y cual el menor \n 4-nuemros A y B, si A es Menor que B sumarlos de lo contrario restar. \n 5-encontrar el cociente entre A y B, Si la division es por cero indicar que no es posible \n 6- Dos numeros A y B, sumarlos si uno de los dos es negativo, de lo contrario multiplicar \n 7-dar un algoritmo que indique si el año es biciesto o no \n 8-Volver al menu anterior \n"))

            elif Condicionales == 2:
                print("indicar cual de los dos numeros es mayor y cual menor")

                Numero1 = int(input("Ingresa el primer numero: "))
                Numero2 = int(input("Ingresa el segundo numero: "))

                if Numero1 == Numero2:
                    print("Los numeros son iguales")
                elif Numero1 > Numero2:
                    print(f"El Numero {Numero1} es Mayor que {Numero2}")
                else:
                    print(f"El Numero {Numero1} es Menor que {Numero2}")
                Condicionales = int(input("1-Identificar si el numero es Positivo o Negativo \n 2-indicar cual de los dos numeros es mayor y cual menor \n 3-indicar de los tres numeros cual es el mayor y cual el menor \n 4-nuemros A y B, si A es Menor que B sumarlos de lo contrario restar. \n 5-encontrar el cociente entre A y B, Si la division es por cero indicar que no es posible \n 6- Dos numeros A y B, sumarlos si uno de los dos es negativo, de lo contrario multiplicar \n 7-dar un algoritmo que indique si el año es biciesto o no \n 8-Volver al menu anterior \n"))

            elif Condicionales == 3:
                print("indicar de los tres numeros cual es el mayor y cual el menor")

                num1 = int(input("Ingresa el primer numero: "))
                num2 = int(input("Ingresa el segundo numero: "))
                num3 = int(input("Ingresa el tercer numero: "))

                if num1 > num2 and num1 > num3:
                    print(f"El numero {num1} es mayor que {num2} y {num3}")
                elif num2 > num1 and num2 > num3:
                    print(f"El numero {num2} es mayor que {num1} y {num3}")
                elif num3 > num1 and num3 > num2:
                    print(f"El numero {num3} es mayor que {num1} y {num2}")
                else:
                    print("Todos los numeros son iguales")
                Condicionales = int(input("1-Identificar si el numero es Positivo o Negativo \n 2-indicar cual de los dos numeros es mayor y cual menor \n 3-indicar de los tres numeros cual es el mayor y cual el menor \n 4-nuemros A y B, si A es Menor que B sumarlos de lo contrario restar. \n 5-encontrar el cociente entre A y B, Si la division es por cero indicar que no es posible \n 6- Dos numeros A y B, sumarlos si uno de los dos es negativo, de lo contrario multiplicar \n 7-dar un algoritmo que indique si el año es biciesto o no \n 8-Volver al menu anterior \n"))

            elif Condicionales == 4:
                print("nuemros A y B, si A es Menor que B sumarlos de lo contrario restar")

                A = int(input("Ingresar el primer numero entero: "))
                B = int(input("ingrese el segundo numero entero: "))

                if A < B:
                    sumar = A + B
                    print("El resultado de la suma es", sumar)
                elif A > B:
                    restar = A - B
                    print("El resultado de la resta es", restar)
                else:
                    print("ingresar dos valores enteros diferentes")
                Condicionales = int(input("1-Identificar si el numero es Positivo o Negativo \n 2-indicar cual de los dos numeros es mayor y cual menor \n 3-indicar de los tres numeros cual es el mayor y cual el menor \n 4-nuemros A y B, si A es Menor que B sumarlos de lo contrario restar. \n 5-encontrar el cociente entre A y B, Si la division es por cero indicar que no es posible \n 6- Dos numeros A y B, sumarlos si uno de los dos es negativo, de lo contrario multiplicar \n 7-dar un algoritmo que indique si el año es biciesto o no \n 8-Volver al menu anterior \n"))

            elif Condicionales == 5:
                print("encontrar el cociente entre A y B, Si la division es por cero indicar que no es posible")

                a = int(input("ingrese el Dividendo: "))
                b = int(input("ingrese el Divisor: "))

                if a == 0:
                    print("No es posible dividir por Cero")
                elif b == 0:
                    print("No es posible dividir por Cero")
                else:
                    Cociente = a / b
                    print("El resultado de la division es " + str(round(Cociente, 2)))
                Condicionales = int(input("1-Identificar si el numero es Positivo o Negativo \n 2-indicar cual de los dos numeros es mayor y cual menor \n 3-indicar de los tres numeros cual es el mayor y cual el menor \n 4-nuemros A y B, si A es Menor que B sumarlos de lo contrario restar. \n 5-encontrar el cociente entre A y B, Si la division es por cero indicar que no es posible \n 6- Dos numeros A y B, sumarlos si uno de los dos es negativo, de lo contrario multiplicar \n 7-dar un algoritmo que indique si el año es biciesto o no \n 8-Volver al menu anterior \n"))

            elif Condicionales == 6:
                print("Dos numeros A y B, sumarlos si uno de los dos es negativo, de lo contrario multiplicar")

                A = int(input("ingresar primer numero: "))
                B = int(input("ingresar segundo numero: "))

                if A >= 0 and B >= 0:
                    Multipicar = A * B
                    print("El valor de la Multiplicacion es: ", Multipicar)
                else:
                    Sumar = A + B
                    print("El valor de la suma es: ", Sumar)
                Condicionales = int(input("1-Identificar si el numero es Positivo o Negativo \n 2-indicar cual de los dos numeros es mayor y cual menor \n 3-indicar de los tres numeros cual es el mayor y cual el menor \n 4-nuemros A y B, si A es Menor que B sumarlos de lo contrario restar. \n 5-encontrar el cociente entre A y B, Si la division es por cero indicar que no es posible \n 6- Dos numeros A y B, sumarlos si uno de los dos es negativo, de lo contrario multiplicar \n 7-dar un algoritmo que indique si el año es biciesto o no \n 8-Volver al menu anterior \n"))

            elif Condicionales == 7:
                print("7-dar un algoritmo que indique si el año es biciesto o no")

                Year = int(input("Indique el año: "))

                def Bisiesto(Year):
                    if Year % 4 == 0 and Year % 100 != 0:
                        return True
                    elif Year % 100 == 0 and Year % 400 == 0:
                        return True
                    else:
                        return False
                print(Bisiesto(Year))
                Condicionales = int(input("1-Identificar si el numero es Positivo o Negativo \n 2-indicar cual de los dos numeros es mayor y cual menor \n 3-indicar de los tres numeros cual es el mayor y cual el menor \n 4-nuemros A y B, si A es Menor que B sumarlos de lo contrario restar. \n 5-encontrar el cociente entre A y B, Si la division es por cero indicar que no es posible \n 6- Dos numeros A y B, sumarlos si uno de los dos es negativo, de lo contrario multiplicar \n 7-dar un algoritmo que indique si el año es biciesto o no \n 8-Volver al menu anterior \n"))

            else:
                print("Por Favor Digite Una Opcion Correcta")
                Condicionales = int(input("1-Identificar si el numero es Positivo o Negativo \n 2-indicar cual de los dos numeros es mayor y cual menor \n 3-indicar de los tres numeros cual es el mayor y cual el menor \n 4-nuemros A y B, si A es Menor que B sumarlos de lo contrario restar. \n 5-encontrar el cociente entre A y B, Si la division es por cero indicar que no es posible \n 6- Dos numeros A y B, sumarlos si uno de los dos es negativo, de lo contrario multiplicar \n 7-dar un algoritmo que indique si el año es biciesto o no \n 8-Volver al menu anterior \n"))

    elif Menuprincipal ==3:
        print("Ciclos")
        Ciclos = int(input("1-Imprimir todos los múltiplos de 3 que hay entre 1 y 100 \n 2-Imprimir los números impares entre 0 y 100 \n 3-Imprimir los números pares del 1 al 100 \n 4-Escribir un programa que imprima por pantalla los cuadrados de los números del 1 al 30 \n 5-Escribir un programa que sume los cuadrados de los cien primeros números naturales mostrando el resultado en pantalla \n 6-Dados dos números naturales, el primero menor que el segundo, generar y mostrar todos los números comprendidos entre ellos en secuencia ascendente \n 7-Sumar todos los números que se digitan por teclado mientras no sea cero \n 8-Volver al menu anterior \n"))
        while Ciclos !=8:

            if Ciclos ==1:
                print("Imprimir todos los múltiplos de 3 que hay entre 1 y 100")
                for i in range(3, 100, 3):
                    print(i)
                Ciclos = int(input("1-Imprimir todos los múltiplos de 3 que hay entre 1 y 100 \n 2-Imprimir los números impares entre 0 y 100 \n 3-Imprimir los números pares del 1 al 100 \n 4-Escribir un programa que imprima por pantalla los cuadrados de los números del 1 al 30 \n 5-Escribir un programa que sume los cuadrados de los cien primeros números naturales mostrando el resultado en pantalla \n 6-Dados dos números naturales, el primero menor que el segundo, generar y mostrar todos los números comprendidos entre ellos en secuencia ascendente \n 7-Sumar todos los números que se digitan por teclado mientras no sea cero \n 8-Volver al menu anterior \n"))

            elif Ciclos ==2:
                print("Imprimir los números impares entre 0 y 100")

                for i in range(1, 100, 2):
                    print(i)
                input()
                Ciclos = int(input("1-Imprimir todos los múltiplos de 3 que hay entre 1 y 100 \n 2-Imprimir los números impares entre 0 y 100 \n 3-Imprimir los números pares del 1 al 100 \n 4-Escribir un programa que imprima por pantalla los cuadrados de los números del 1 al 30 \n 5-Escribir un programa que sume los cuadrados de los cien primeros números naturales mostrando el resultado en pantalla \n 6-Dados dos números naturales, el primero menor que el segundo, generar y mostrar todos los números comprendidos entre ellos en secuencia ascendente \n 7-Sumar todos los números que se digitan por teclado mientras no sea cero \n 8-Volver al menu anterior \n"))

            elif Ciclos ==3:
                print("Imprimir los números pares del 1 al 100")

                for i in range(2, 101, 2):
                    print(i)
                input()
                Ciclos = int(input("1-Imprimir todos los múltiplos de 3 que hay entre 1 y 100 \n 2-Imprimir los números impares entre 0 y 100 \n 3-Imprimir los números pares del 1 al 100 \n 4-Escribir un programa que imprima por pantalla los cuadrados de los números del 1 al 30 \n 5-Escribir un programa que sume los cuadrados de los cien primeros números naturales mostrando el resultado en pantalla \n 6-Dados dos números naturales, el primero menor que el segundo, generar y mostrar todos los números comprendidos entre ellos en secuencia ascendente \n 7-Sumar todos los números que se digitan por teclado mientras no sea cero \n 8-Volver al menu anterior \n"))

            elif Ciclos ==4:
                print("Escribir un programa que imprima por pantalla los cuadrados de los números del 1 al 30")


                def Generar_cuadrados(n):
                    if 2 * n <= 30:
                        Cuadrados = [i ** 2 for i in range(1, 31)]
                        return Cuadrados[:n] + Cuadrados[-n:]

                resultado = Generar_cuadrados(15)
                print(resultado)
                Ciclos = int(input("1-Imprimir todos los múltiplos de 3 que hay entre 1 y 100 \n 2-Imprimir los números impares entre 0 y 100 \n 3-Imprimir los números pares del 1 al 100 \n 4-Escribir un programa que imprima por pantalla los cuadrados de los números del 1 al 30 \n 5-Escribir un programa que sume los cuadrados de los cien primeros números naturales mostrando el resultado en pantalla \n 6-Dados dos números naturales, el primero menor que el segundo, generar y mostrar todos los números comprendidos entre ellos en secuencia ascendente \n 7-Sumar todos los números que se digitan por teclado mientras no sea cero \n 8-Volver al menu anterior \n"))

            elif Ciclos ==5:
                print("Escribir un programa que sume los cuadrados de los cien primeros números naturales mostrando el resultado en pantalla")

                c=0
                s=0
                while (c<100):
                    c=c+1
                    s=s+c**2
                print("La suma de los cuadrados es: ",s)
                Ciclos = int(input("1-Imprimir todos los múltiplos de 3 que hay entre 1 y 100 \n 2-Imprimir los números impares entre 0 y 100 \n 3-Imprimir los números pares del 1 al 100 \n 4-Escribir un programa que imprima por pantalla los cuadrados de los números del 1 al 30 \n 5-Escribir un programa que sume los cuadrados de los cien primeros números naturales mostrando el resultado en pantalla \n 6-Dados dos números naturales, el primero menor que el segundo, generar y mostrar todos los números comprendidos entre ellos en secuencia ascendente \n 7-Sumar todos los números que se digitan por teclado mientras no sea cero \n 8-Volver al menu anterior \n"))

            elif Ciclos ==6:
                print("Dados dos números naturales, el primero menor que el segundo, generar y mostrar todos los números comprendidos entre ellos en secuencia ascendente")


                num1 = int(input("escriba el primer numero: "))
                num2 = int(input("escriba el segundo numero: "))

                if num2 > num1:
                    print(list(range(num1 +1 , num2)))
                else:
                    print("el  primer numero debe ser menor al segundo")

                Ciclos = int(input("1-Imprimir todos los múltiplos de 3 que hay entre 1 y 100 \n 2-Imprimir los números impares entre 0 y 100 \n 3-Imprimir los números pares del 1 al 100 \n 4-Escribir un programa que imprima por pantalla los cuadrados de los números del 1 al 30 \n 5-Escribir un programa que sume los cuadrados de los cien primeros números naturales mostrando el resultado en pantalla \n 6-Dados dos números naturales, el primero menor que el segundo, generar y mostrar todos los números comprendidos entre ellos en secuencia ascendente \n 7-Sumar todos los números que se digitan por teclado mientras no sea cero \n 8-Volver al menu anterior \n"))

            elif Ciclos ==7:
                print("Sumar todos los números que se digitan por teclado mientras no sea cero")

                Sumar=0
                n=int(input("ingrese los numero a sumar(0 para finalizar): "))
                while n !=0:
                    if n > 0:
                        Sumar+= n
                        n=int(input("ingrese los numero a sumar(0 para finalizar): "))


                print("la suma de los nuemrois digitados es: " , Sumar)

                Ciclos = int(input("1-Imprimir todos los múltiplos de 3 que hay entre 1 y 100 \n 2-Imprimir los números impares entre 0 y 100 \n 3-Imprimir los números pares del 1 al 100 \n 4-Escribir un programa que imprima por pantalla los cuadrados de los números del 1 al 30 \n 5-Escribir un programa que sume los cuadrados de los cien primeros números naturales mostrando el resultado en pantalla \n 6-Dados dos números naturales, el primero menor que el segundo, generar y mostrar todos los números comprendidos entre ellos en secuencia ascendente \n 7-Sumar todos los números que se digitan por teclado mientras no sea cero \n 8-Volver al menu anterior \n"))

    else:
        print("Por Favor Digite Una Opcion Correcta")
    Menuprincipal = int(input("Menu: \n 1-Operadores \n 2-Condicionales \n 3-Ciclos \n 99-Salir del Menu \n "))





