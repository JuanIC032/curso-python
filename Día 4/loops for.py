# concepto 'iterable'
# dos tipos de loops. 1 los que se repiten una cantidad definida de veces y 2 los que se
# repiten infinitas veces, esos son 1(for) y 2(while)

#Usando click derecho en una variable, luego yendo a refactor y finalmente en rename,
# puedo cambiar el nombre de una variable en todo el codigo

lista = ['a', 'b', 'c', 'd']
for letra in lista:
    numero_letra = lista.index(letra) + 1
    print(f'Letra {numero_letra}: {letra}')

print('\n')

# Las variables van cambiando en cada vuelta del loop

lista = ['pablo', 'laura', 'fede', 'luis', 'julia']

for nombre in lista:
    if nombre.startswith('l'):
        print(nombre)
    else:
        print('Nombre que no comienza con L')

print('\n')

numeros = [1,2,3,4,5]
mi_valor = 0

for numero in numeros:
    mi_valor = mi_valor + numero

print(mi_valor) #importante que este print este fuera del loop,
# hay que tener cuiddado siemmpre con las tabulaciones
print('\n')

palabra = 'python'

for letra in palabra:
    print(letra)

print('\n')

palabra = 'python es genial'

for letra in palabra:
    print(letra)

print('\n')

for letra in 'python':
    print(letra)

for letra in [1,2,3]:
        print(letra)

for letra in (1,2,3):
    print(letra)

for objeto in [[1,2],[3,4],[5,6]]:
        print(objeto)

print('\n')

for a, b in [[1,2],[3,4],[5,6]]:
        print(a)
        print(b)

print('\n')

dic = {'clave1': 'a', 'clave2': 'b', 'clave3' : 'c'}
for item in dic:
    print(item)

dic = {'clave1': 'a', 'clave2': 'b', 'clave3' : 'c'}
for item in dic.items():
    print(item)

dic = {'clave1': 'a', 'clave2': 'b', 'clave3' : 'c'}
for item in dic.values():
    print(item)

dic = {'clave1': 'a', 'clave2': 'b', 'clave3' : 'c'}
for a,b in dic.items():
    print(a,b)