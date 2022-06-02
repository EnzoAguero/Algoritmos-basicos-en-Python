""" Prueba ejercicio 3 -  """

""" Prueba ejercicio 4 - programa que pasa de temperatura F° a C° """

""" grados = float(input('Ingrese cuantos grados F°: '))
resultado = ''

resultado = (grados-32) * 5 / 9 
resultado = round(resultado)
print(resultado) """

""" Prueba ejercicio 5 - Este programa el usuario ingresa 5 numeros y suma los numeros de la posicion num 3,4 y 5 """

""" arreglo = []
while len(arreglo) >= 0 and len(arreglo) < 5:
    numero = int(input('Ingrese un numero: '))
    arreglo.append(numero)
    print(arreglo)

print('************* Suma del arreglo **************')

num1 = arreglo[2]
num2 = arreglo[3]
num3 = arreglo[4]
resultado = num1 + num2 + num3
print(num1,num2,num3)
print(resultado) """

""" Prueba ejercicio 6 - Programa que verifica si algun numero de la lista es par """

""" numeros = [1,2,3,4,5,6,8,9,10]

def esPar(): 
    print(numeros)
for i in numeros:
     if(i%2 == 0):
       print(i,'es par') """

""" Prueba ejercicio 7 - Programa que verifica que dos palabras son iguales """

""" palabra1 = input('Ingrese una palabra ')
palabra2 = input('Ingrese una segunda palabra ')

if(palabra1 == palabra2):
    print('Las palabras son iguales')
else:
    print('las palabras no son iguales') """

""" Prueba ejercicio 8 - Este programa tiene tus dias de descanso y depende el dia ingresado te avisa si te toca descansar o levantar la pala """

""" dia = input('Ingrese un dia de la semana ')

mensajeDescanso = 'Dia de descanso!!!'
mensajeLaburo = 'A laburar!!!'

descanso ='lunesviernessabadodomingo'
descanso2 = ['lunes','viernes','sabado','domingo']      ##Dos formas

 if(dia in descanso2):                                   ##dia in descanso funciona igual
    print('Hoy es', dia ,mensajeDescanso)
else:
    print(mensajeLaburo)  """
""" 
for i in descanso2:
    if(dia == i):
        print('Hoy es', i , mensajeDescanso)                ##Otra forma aplicando un for """


""" Ejercicio 9 - Este programa te dice si un numero es capicua o no """


""" numero = int(input('Ingrese un numero '))
numPrincipal = numero

resultado = False
numero = str(numero)                
numero = numero[::-1]               ##Me da vuelta el numero
numero = int(numero)            
print(numero)
print(numPrincipal)

if(numero == numPrincipal):
    resultado = True
    print(resultado)
else:
    resultado = False
    print(resultado) """

""" Ejercicio 10 - Retorna si A es menor a B """

""" a = int(input('Ingrese un primer numero: '))
b = int(input('Ingrese un segundo numero: '))

menor = False
if(a < b):
    menor = True
    print(menor)
else:
    menos = False
    print(menor) """
    
""" Ejercicio 11 - Define si el resultado de una multiplicacion del numero A con el numero B. Es igual a la
division del numero A con el numero B """

""" a = int(input('Ingrese un numero: '))
b = int(input('Ingrese un segundo numero: '))

multiplicacion = a*b
division = a/b

if(multiplicacion == division):
    print('es igual')

else:
    print('no son iguales') """

""" ejercicio 12 - ejercicio que retorna si dos o mas numeros estan en dos listas """
""" 
listaA = [1,2,3,4,5]
listaB = [3,5,1,7,8]

for i in listaA:
    for j in listaB:
        if (i == j):
            print(i, 'esta en las dos listas') """
 
""" Ejercicio 13 - programa que recibe una palabra y la retorna al revez"""
""" 
palabra = input('Ingrese una palabra ')

print(palabra)
palabra = palabra[::-1]
print(palabra) """

""" ejercicio 14 - programa que reciba una palabra e intercambia vocales por "x" """

""" palabra = input('Ingrese una palabra ')

vocales = 'aeiou'
nueva=''

for letra in palabra:
    if(letra not in vocales):
        nueva += letra
    else:
        nueva += 'x'
print(nueva) """

""" ejercicio 15 - busca una palabra en una oracion y la cambia por una random """
""" 
oracion = input('Escriba una oracion: ')
palabra = input('Escriba alguna palabra que se encuentra en la oracion: ')


for i in oracion:
    if(palabra not in oracion):
        palabra = palabra
    else:
        palabra = 'enzo'
    print(oracion) """
""" TERMINARRRRR """

""" Ejercicio 16 - programa que reverse una lista """
""" 
lista = ['Manzana','Pera','Banana','Naranja']
lista = lista[::-1]
print(lista) """

""" Ejercicio 17 - programa que busca un elemento de una lista pasado como parametro """


""" lista = ['Manzana','Pera','Banana','Naranja']
def busqueda(elemento,array):
    for index in array:
        if(index == elemento):
            return index

print(busqueda('Banana',lista)) """

""" Ejercicio 18 - Programa donde el usuario ingresa el tamaño de un arreglo y un numero y devuelve la tabla de ese numero con el tamaño del arreglo"""


""" arreglo = int(input('Indique el tamaño del arreglo: '))
num = int(input('Ingrese el numero de la tabla que desee ver: '))
lista=[]

while len(lista) >= 0 and len(lista) < arreglo:
    for i in range (1,arreglo+1):
        i = num*i
        lista.append(i)
print(lista) """

""" Ejercicio 19 -  """

""" lista = [1,2,5,8,3,30,9,13]
print(lista)
for i in lista:
    if(i%2==1 and i >7):
        print(i) """

""" Ejercicio 20 -  """

lista = [20,15,12,11,8,4,1]
menor = lista[0]

for n in lista:
    if(menor > n):
        menor = n
        print(menor)
    