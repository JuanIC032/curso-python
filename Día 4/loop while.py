monedas = 5

while monedas > 0:
    print(f'Tengo {monedas} monedas')
    monedas -= 1
else:
    print('No tengo más monedas')

print('\n')

respuesta = 's'

while respuesta == 's':
    respuesta= input('quieres seguir? (s/n)')
else:
    print('Gracias')

while respuesta == 's':
    pass


print('hola')

nombre = input('Tu nombre: ')

for letra in nombre:
    if letra == 'r':
        break
    print(letra)

print('\n')

for letra in nombre:
    if letra == 'r':
        continue
    print(letra)