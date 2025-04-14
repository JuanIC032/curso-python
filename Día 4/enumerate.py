lista = ['a','b','c']
indice = 0
for item in lista:
    print(indice,item)
    indice += 1

print('\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

lista = ['a','b','c']
for item in enumerate(lista):
    print(item)

print('\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

lista = ['a','b','c']
for item in enumerate(range(50,55)):
    print(item)

print('\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

lista = ['a','b','c']

mis_tuples = list(enumerate(lista))
print(mis_tuples)

print('\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

lista_indices = list(enumerate('Python'))
print(lista_indices)

print('\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for nombre in enumerate(lista_nombres):
    if nombre[1].startswith('M'):
        print(nombre[0])