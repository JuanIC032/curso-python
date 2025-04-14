mi_lista = ['a','b','c']
print(type(mi_lista))

otra_lista = ['hola',55,5.8]

resultado = len(mi_lista)
print(resultado)

resultado = mi_lista[0]
print(resultado)

resultado = mi_lista[0:2]
print(resultado)

resultado = mi_lista[0:]
print(resultado)

mi_lista2 = ['d', 'e','f']
print(mi_lista+mi_lista2)

mi_lista3 = mi_lista + mi_lista2
print(mi_lista3)

mi_lista3[0] = 'alfa'
print(mi_lista3)

mi_lista3[0] = 'a'

# Esto no es una concatenación, es una modificación directa de la lista, lo cual no podemos hacer
# con los strings
mi_lista3.append('g')
print(mi_lista3)

mi_lista3 = mi_lista + mi_lista2

# '.pop' sirve para eliminar un objeto de una lista, si dejamos vacio los parentesis, se eliminara
# el ultimo elemento de la lista
mi_lista3.pop()
print(mi_lista3)
# en este caso se eliminó la 'g' ya que era el ultimo elemento de la lista

mi_lista3 = mi_lista + mi_lista2

# en este caso al indicar el indice cero, se elimino el primer elemento de la lista
mi_lista3.pop(0)
print(mi_lista3)

mi_lista3 = mi_lista + mi_lista2

# podemos guardar el elemento eliminado en una variable
eliminado = mi_lista3.pop(0)
print(eliminado)

# metodos mas importantes
# '.sort' sirve para ordenar listas, en este caso se ordenaron las letras alfabeticamente
lista = ['g','o','b','m','c']
lista.sort()
print(lista)

# '.sort' es un metodo que no devuelve ni un valor como tal, ejemplo:
lista = ['g','o','b','m','c']
nueva_lista = lista.sort()
print(nueva_lista) #esto devuelve como resultado 'None', osea nada
print(type(nueva_lista)) # 'NonType' es este tipo de dato, es decir es nada
# '.sort' realiza la acción de ordenar la lista que le damos, pero no devuelve ningún valor
# y este 'no valor' no lo podemos asignar a variables

# Hay métodos que realizan acciones pero no devuelven valores que se puedan almacenar

# este metodo ordena las listas en reversa
lista.reverse()
print(lista)