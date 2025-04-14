mi_set = set([1,2,3,4,5])
print(type(mi_set))
print(mi_set)

otro_set = {1,2,3}
print(type(otro_set))
print(otro_set)

mi_set = set([1,2,3,4,5,1,1,3,2,1,2,3,2,1])
print(type(mi_set))
print(mi_set)

# No podemos poner ni listas ni diccionarios en los sets
# Pero si admite tuples

mi_set = set([1,2,3,4,5,(1,2,3),1,3,2,1,2,3,2,1])
print(type(mi_set))
print(mi_set)

mi_set = set([1,2,3,4,5])
print(len(mi_set))
print(2 in mi_set)

s1 = {1,2,3}
s2 = {3,4,5}
s3 = s1.union(s2)
print(s3)

print(s1)
s1.add(4)
print(s1)

s1.add(2)
print(s1)

s1 = {1,2,3}
s1.remove(3)
print(s1)

# .discard funciona igual a .remove, la unica diferencia es que cuando le damos un valor que no esta en el set
# .remove nos dará un error, mientras .discard simplemente no hará nada
s1.discard(6)
print(s1)

s1 = {1,2,3 }
s1.pop()
print(s1)

s1 = {1,2,3}
s1.clear()
print(s1)