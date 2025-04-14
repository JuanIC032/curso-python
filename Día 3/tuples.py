mi_tuple = (1,2,3,4)
print(type(mi_tuple))

t = 5, 5.6, 'ff'

print(mi_tuple[0])
print(mi_tuple[-2])

#mi_tuple[0] = 5 Los tuples son inmutables

mi_tuple = (1,2,(10,20),4)
print(mi_tuple)
print(mi_tuple[2])
print(mi_tuple[2][0])

mi_tuple = list(mi_tuple)
print(type(mi_tuple))

mi_tuple = tuple(mi_tuple)
print(type(mi_tuple))

t = (1,2,3)

x,y,z = t
print(x,y,z)

t = (1,2,3,1)
print(len(t))
print(t.count(1)) # .count sirve para contar la cantidad de veces que aparece un determinado elemento
print(t.index(2))
