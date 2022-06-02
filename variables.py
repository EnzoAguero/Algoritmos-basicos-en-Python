 ## Comentarios

 # <- single line commment

"""
 comentario
 de a muchas lineas
 
"""

### Asignacion variable unica
print()

nombre = "Enzo"
print('Hola ' + nombre)


## Data Types ##

Listas = ['cosa1','cosa2','cosa3'] ##Ordenadas, intercambiables, permiten duplicado
Tupla = ('Cosa4','cosa5','Cosa6') ##Ordenadas, no permiten cambios
Set1 = {'Cosa7','cosa8','cosa9'} ##Desordenados, no permiten cambios,no tiene index
Dictionary = {                   ##Ordenados, sin index, permite cambios
        'cosaUno' : 1,
        'cosaDos' : 2,
        'cosaTres' : 'tres'
}                 

## Slices ## //Corta segun donde vos le digas

##a[start:stop]
##a[start:]
##a[:stop]
##a[:]

print(Listas[::-1]) ##Da vuelta una lista o string
print(Listas[1:2])  ##Me devuelve el primer elemento, no cuenta el 2
print(Listas[2:])



##Casting

#Convertir un tipo de dato a otro

##str()
##float()
##int()
##type(list(tupla))