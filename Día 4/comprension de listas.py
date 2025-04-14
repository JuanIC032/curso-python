palabra = 'python'

lista = []

for letra in palabra:
    lista.append(letra)

print(lista)

print('\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

palabra = 'python'

lista = [letra for letra in palabra]
print(lista)

lista = [letra for letra in 'python']
print(lista)

lista = [n for n in range(0,21,2)]
print(lista)

lista = [n / 2 for n in range(0,21,2)]
print(lista)

lista = [n for n in range(0,21,2) if n * 2 > 10]
print(lista)

lista = [n  if n * 2 > 10 else 'no' for n in range(0,21,2)]
print(lista)

print('\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

pies = [10,20,30,40,50]
metros = [round((n / 3.281), 2) for n in pies]
print(metros)

print('\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_pares = [n for n in valores if n%2 == 0]
print(valores_pares)