# imprimir
print("Hola mundo")
print( "resultado: ", 55+100, " manzanas" )

# string - palabras
palabra = "hola"
# int - numeros enteros
edad = 23
# float - numeros decimales
km = 1.55
# boolean/boleano - verdarero o falso / true or false
culpable = True

#------
min= 20
seg=12
# print(min+":"+seg)



##----------
## OPERACIONES
## -------

## NUMERICAS + - * /

## comparacion
## igual ==
## diferente !=
## mayor que >
## menor que <
## mayor o igual >=
## menor o igual <=

#logico if - comparacion
x=11
y=12


if(x>y>0): #  x>y and y>0
    print("si es nomalito")
else:
    print("no es")
## or - cualquiera debe ser verdaro para que todo sea verdadero.
## si todo es falso , resultado falso
if(x>y or y>20 or x>50): #  x>y or y>0
    print("si es con or")
else:
    print("no es con or")

## and - todo debe ser verdadero para que el resultado sea verdadero
## si uno solo es falso, solo se vuelve falso.

if(x>y and y>0 and x>0): #  x>y or y>0
    print("si es con and")
else:
    print("no es con and", 0.22)


## convertir variables

# int a string
xPalabra = str(x)
print("esto es: ", xPalabra, "es de tipo", type(xPalabra))

# convertir string a int
cosa = "2500"
print(type(cosa))
print( 5 + int(cosa) )

cosa2 = input()

print("cosa2 es de tipo: ",type(cosa2) , "y su valor es: ", cosa2)
print( int(cosa2) + 9000  )