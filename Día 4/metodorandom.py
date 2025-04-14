from random import *

aletorio = randint(1,50)
print(aletorio)

print('\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

aletorio = uniform(1,5)
print(aletorio)

aletorio = round(uniform(1,5), 1)
print(aletorio)

aletorio = random()
print(aletorio)

print('\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

colores = ['azul', 'rojo', 'verde', 'amarillo']
aleatorio = choice(colores)
print(aleatorio)

print('\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

numeros = list(range(5,50,5))
shuffle(numeros)
print(numeros)
