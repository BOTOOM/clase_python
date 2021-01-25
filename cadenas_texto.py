gato = "miau"
perro = "guau"


## tamaño de la palabra
# print( len(gato))
# print("gato igual 4:", len(gato) == 4 )
# print("-----------------")
print("perro igual a gato", len(gato) == len(perro) )
print("-----------------")

## unir (concatenar), textos

animales = gato+ " " + perro
print(animales)

## volver todo mayuscula
print(animales.upper())
print("sds" ,animales.format("g","J"))

##  remplazar una variable
txt = "For only {price} dollars!"
print(txt.format(price = 49))

## remplazar letras o palabras
perro2="perro"
print(perro2.replace("r","R"))


## separar palabras
frase = "te amo muchisimo"

print( frase.split() )
print( frase.split("amo") )

frase2= "como es?, como seria?, como fue?"
frase3= frase2.split(",")
print(frase3)
print(frase3[0].split())
