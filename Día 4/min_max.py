menor = min(58,96,72,64,35)
mayor = max(58,96,72,64,35)
print(menor,mayor)

print('\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

lista = [58,96,72,64,35]
print(max(lista))

print('\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

lista = [58,96,72,64,35]
print(f'El menor es {min(lista)} y el mayor es {max(lista)}')


print('\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

nombres = ['juan','pablo', 'alicia', 'carlos']

print(min(nombres))

print('\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

nombre = 'Carlos'
print(min(nombre)) # min busca en orden alfabetico, uno pensaria que en
# este caso deberia devolver la letra 'a' pero devuelve la 'C' por que primero busca en las letras mayúsculas
nombre = 'carlos'
print(min(nombre))
nombre = 'carlOs'
print(min(nombre))
nombre = 'Carlos'
print(min(nombre.lower()))

print('\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

dic = {'C1':45, 'C2':11}
print(min(dic))

dic = {'C1':45, 'C2':11}
print(min(dic.values()))

print('\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2,"Darío":49}

edad_minima = min(diccionario_edades.values())
ultimo_nombre = max((diccionario_edades.keys()))
print(edad_minima)