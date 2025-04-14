texto= 'ABCDEFGHIJKLM'
fragmento = texto[2]
print(fragmento)

#En este caso le indico a python que extraiga los caracteres desde el indice 2 hasta el 4
texto= 'ABCDEFGHIJKLM'
fragmento = texto[2:5]
print(fragmento)

#si omitimos el segundo factor y dejamos solamente los dos puntos, python extraerá
# desde el indice 2 hasta el final del string
texto= 'ABCDEFGHIJKLM'
fragmento = texto[2:]
print(fragmento)

#lo mismo al revés
texto= 'ABCDEFGHIJKLM'
fragmento = texto[:5]
print(fragmento)

#El tercer factor indica cada cuantos caracteres se va a extraer un caracter
texto= 'ABCDEFGHIJKLM'
fragmento = texto[2:10:2]
print(fragmento)

#si colocamos un número negativo tendremos un orden inverso
texto= 'ABCDEFGHIJKLM'
fragmento = texto[::-1]
print(fragmento)