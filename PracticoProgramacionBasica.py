### 1 
""" 
sexo = input('Ingrese su sexo por favor ')
sexo = sexo.upper()

def identificador(sexo):
    if(sexo == 'masculino' or sexo == 'm'):
        return True
    else:
        return False

print(identificador(sexo)) """

### 2

from ast import Try
import os
clear = lambda: os.system('cls')

def Pantalla1():
    clear()
    active = False
    while not active:
        
        try:
            palabra = input('Introduzca su sexo: ')
            if(palabra == 'masculino' or palabra == 'm' or palabra == 'femenino' or palabra == 'f'):
                
                print(True)
            else:
                
                print(False)
            print('Desea continuar: S/N')
            opcion = input()
            if(opcion == 'N' or opcion == 'n'):
                active = True
        except:
            print('Por favor introduzca una palabra o letra')

def Pantalla2():
    clear()
    active = False
    while not active:
        
        try:
            edad = int(input('Ingrese su edad: '))
            if(edad >= 18):
                print(True)
            else:
                
                print(False)
            print('Desea continuar: S/N')
            opcion = input()
            if(opcion == 'N' or opcion == 'n'):
                active = True
        except:
            print('Por favor introduzca un numero')

def Pantalla3():
    clear()
    active = False
    while not active:
        
        try:
            edad = int(input('Ingrese su edad: '))
            if(edad < 10 or edad > 60):
               
                print(True)
            else:
                
                print(False)
            print('Desea continuar: S/N')
            opcion = input()
            if(opcion == 'N' or opcion == 'n'):
                active = True
        except:
            print('Por favor introduzca un numero')

def Pantalla4():
    clear()
    active = False
    while not active:
        try:
            grados = float(input('Ingrese cuantos grados F°: '))
            resultado = ''
            resultado = (grados-32) * 5 / 9 
            resultado = round(resultado)
            print(resultado)

            print('Desea continuar: S/N')
            opcion = input()
            if(opcion == 'N' or opcion == 'n'):
                active = True
        except:
                print('Por favor introduzca la temperatura')

def Pantalla5():
    clear()
    active = False
    while not active:
        try:
          
            arreglo = []
            while len(arreglo) >= 0 and len(arreglo) < 5:
                numero = int(input('Ingrese un numero: '))
                arreglo.append(numero)
                print(arreglo)

            print('*** Siguiente parte: Suma de los ultimos 3 numeros ***')
            
            num1 = arreglo[2]
            num2 = arreglo[3]
            num3 = arreglo[4]
            resultado = num1 + num2 + num3
            print(num1,num2,num3)
            print(resultado) 
            if(resultado%2 == 0):
                print(True)
            else: 
                
                print(False)

            print('Desea continuar: S/N')
            opcion = input()
            if(opcion == 'N' or opcion == 'n'):
                active = True
        except:
                print('Debes ingresar 5 numeros')

def Pantalla6():
    clear()
    active = False
    while not active:      
        try:
            arreglo = []
            while len(arreglo) >= 0 and len(arreglo) < 5:
                numero = int(input('Ingrese un numero: '))
                arreglo.append(numero)
                print(arreglo)

            print(arreglo)
            for i in arreglo:
                if(i%2 == 0):
                 print(i,True)
                else:
                     print(i,False)
            print('Desea continuar: S/N')
            opcion = input()
            if(opcion == 'N' or opcion == 'n'):
                active = True
        except:
            print('nada')

def Pantalla7():
    clear()
    active = False
    while not active:
        try:
            palabra1 = input('Ingrese una palabra ')
            palabra2 = input('Ingrese una segunda palabra ')
            igualdad = False
            if(palabra1 == palabra2):
                igualdad = True
                print(igualdad)
            else:
                igualdad = False
                print(igualdad)

            print('Desea continuar: S/N')
            opcion = input()
            if(opcion == 'N' or opcion == 'n'):
                active = True
        except:
            print('nada')
        
def Pantalla8():
    clear()
    active = False
    while not active:
        try:
            dia = input('Ingrese un dia de la semana ')
            descanso2 = ['lunes','viernes','sabado','domingo']
            mensajeDescanso = 'Dia de descanso!!!'
            mensajeLaburo = 'A laburar!!!'
            if(dia in descanso2):                                  
                print('Hoy es', dia ,mensajeDescanso)
            else:
                print(mensajeLaburo) 

            print('Desea continuar: S/N')
            opcion = input()
            if(opcion == 'N' or opcion == 'n'):
                active = True
        except:
                print('Ingrese un dia de la semana por favor')

def Pantalla9():
    clear()
    active = False
    while not active:
        try:
            numero = int(input('Ingrese un numero: '))
            numPrincipal = numero

            
            numero = str(numero)
            numero = numero[::-1]
            numero = int(numero)      ##Si no lo paso devuelta a int no se puede. porque compara un int con un str
            print(numero)
            print(numPrincipal)

            if(numero == numPrincipal):
                
                print(True)
            else:
                
                print(False)

                print('Desea continuar: S/N')
                opcion = input()
                if(opcion == 'N' or opcion == 'n'):
                    active = True
        except:
                print('Nada')

def Pantalla10():
    clear()
    active = False
    while not active:
        try:
            a = int(input('Ingrese un primer numero: '))
            b = int(input('Ingrese un segundo numero: '))

            
            if(a < b):
                
                print(True)
            else:
                
                print(False)

            print('Desea continuar: S/N')
            opcion = input()
            if(opcion == 'N' or opcion == 'n'):
                active = True
        except:
            print('Por favor ingrese numeros')

def Pantalla11():
    clear()
    active = False
    while not active:
        try:
            a = int(input('Ingrese un numero: '))
            b = int(input('Ingrese un segundo numero: '))

            multiplicacion = a*b
            division = a/b

            if(multiplicacion == division):
                    print(True)

            else:
                    print(False)
            print('Desea continuar: S/N')
            opcion = input()
            if(opcion == 'N' or opcion == 'n'):
                active = True        
        except:
                print('nada')

def Pantalla12():
    clear()
    active = False
    while not active:
        try:
            listaA = [1,2,3,4,5]
            listaB = [3,5,1,7,8]

            print(listaA)
            print(listaB)   
            for i in listaA:
                for j in listaB:
                    if (i == j):
                        print(i, 'esta en las dos listas')
            print('Desea continuar: S/N')
            opcion = input()
            if(opcion == 'N' or opcion == 'n'):
                active = True  
        except:
            print('nada')

def Pantalla13():
    clear()
    active = False 
    while not active:
        try:
            palabra = input('Ingrese una palabra ')

            print(palabra)
            palabra = palabra[::-1]
            print(palabra)
            print('Desea continuar: S/N')
            opcion = input()
            if(opcion == 'N' or opcion == 'n'):
                active = True  
        except: 
            print('nada')  
                    
def Pantalla14():
    clear()
    active = False 
    while not active:
        try:
            palabra = input('Ingrese una palabra ')

            vocales = 'aeiou'
            nueva=''

            for letra in palabra:
                if(letra not in vocales):
                    nueva += letra
                else:
                    nueva += 'x'
            print(nueva)
            print('Desea continuar: S/N')
            opcion = input()
            if(opcion == 'N' or opcion == 'n'):
                active = True  
        except: 
            print('nada')

def Pantalla15():
    clear()
    active = False 
    while not active:
        try:
            print('Desea continuar: S/N')
            opcion = input()
            if(opcion == 'N' or opcion == 'n'):
                active = True  
        except: 
            print('nada')

def Pantalla16():
    clear()
    active = False 
    while not active:
        try:
            lista = ['Manzana','Pera','Banana','Naranja']
            print('lista original: ', lista,'\n',end="")
            lista = lista[::-1]
            print(lista)
            print('Desea continuar: S/N')
            opcion = input()
            if(opcion == 'N' or opcion == 'n'):
                active = True  
        except: 
            print('nada')

def Pantalla17():
    clear()
    active = False 
    while not active:
        try:
            lista = ['manzana','pera','banana','naranja']
            elem = input('Puede buscar: manzana, pera, banana, naranja: ')
            def busqueda(elemento,array):
                for index in array:
                    if(index == elemento):
                        return index
            print(lista)
            print(busqueda(elem,lista))
            print('Desea continuar: S/N')
            opcion = input()
            if(opcion == 'N' or opcion == 'n'):
                active = True  
        except: 
            print('nada')

def Pantalla18():
    clear()
    active = False 
    while not active:
        try:
            arreglo = int(input('Indique el tamaño del arreglo: '))
            num = int(input('Ingrese el numero de la tabla que desee ver: '))
            lista=[]

            while len(lista) >= 0 and len(lista) < arreglo:
                for i in range (1,arreglo+1):
                    i = num*i
                    lista.append(i)
            print(lista)

            print('Desea continuar: S/N')
            opcion = input()
            if(opcion == 'N' or opcion == 'n'):
                active = True  
        except: 
            print('nada')

def Pantalla19():
    clear()
    active = False 
    while not active:
        try:
            lista = [1,2,5,8,3,30,9,13]
            print(lista)
            for i in lista:
                if(i%2==1 and i >7):
                    print(i)

            print('Desea continuar: S/N')
            opcion = input()
            if(opcion == 'N' or opcion == 'n'):
                active = True  
        except: 
            print('nada')

def Pantalla20():
    clear()
    active = False 
    while not active:
        try:

            lista = [20,15,12,11,8,4,1]
            menor = lista[0]
            print(lista)
            for n in lista:
                if(menor > n):
                    menor = n
            print('El menor es: ',menor)
            print('Desea continuar: S/N')
            opcion = input()
            if(opcion == 'N' or opcion == 'n'):
                active = True  
        except: 
            print('nada')










active = False
while not active:
    clear()
    print('Programa basico:')
    print('1 - Sexo')
    print('2 -  Un programa que recibe la edad de una persona y retorna True si es mayor de 18 años o false si es menor.')
    print('3 - Un programa que reciba una edad y retorne True si es menor a 10 o mayor a 60 en caso contrario retornara False.')
    print('4 - Conversion de F° a C°')
    print('5 - Suma de 3 ultimos numeros de un arreglo')
    print('6 - numero par')
    print('7 - palabras iguales')
    print('8 - dia de semana')
    print('9 - numero capicua')
    print('10 - Indica si A es menor a B')
    print('11 - multiplicacion igual a division')
    print('12 - retorna dos numeros qe estan en la lista')
    print('13 - programa que recibe una palabra y la retorna al revez')
    print('14 - programa que reciba una palabra e intercambia vocales por "x" ')
    print('15 - busca una palabra en una oracion y la cambia por una random')
    print('16 - programa que reverse una lista')
    print('17 -  programa que busca un elemento de una lista pasado como parametro')
    print('18 -Programa donde el usuario ingresa el tamaño de un arreglo y un numero y devuelve la tabla de ese numero con el tamaño del arreglo')
    print('19 - Imprime en pantalla programáticamente los números impares mayores a 7.')
    print('20 - Elimine la nota más baja programáticamente sin usar la función (min) y escriba en pantalla. Luego programáticamente calcule el promedio de notas descontando la nota eliminada')
    print('21 - Exit')
    opcion = input('Introduce un numero:')
    try:
        if int(opcion) == 1:
            Pantalla1()
        elif int(opcion) == 2:
            Pantalla2()
        elif int(opcion) == 3:
            Pantalla3()
        elif int(opcion) == 4:
            Pantalla4()
        elif int(opcion) == 5:
            Pantalla5()
        elif int(opcion) == 6:
            Pantalla6()
        elif int(opcion) == 7:
            Pantalla7()
        elif int(opcion) == 8:
            Pantalla8()
        elif int(opcion) == 9:
            Pantalla9()
        elif int(opcion) == 10:
            Pantalla10()
        elif int(opcion) == 11:
            Pantalla11()
        elif int(opcion) == 12:
            Pantalla12()
        elif int(opcion) == 13:
            Pantalla13()
        elif int(opcion) == 14:
            Pantalla14()
        elif int(opcion) == 15:
            Pantalla15()
        elif int(opcion) == 16:
            Pantalla16()
        elif int(opcion) == 17:
            Pantalla17()
        elif int(opcion) == 18:
            Pantalla18()
        elif int(opcion) == 19:
            Pantalla19()
        elif int(opcion) == 20:
            Pantalla20()
        elif int(opcion) == 21:
            print('Saliendo')
            active = True   
    except:
        print("Por favor introduzca una opcion valida")