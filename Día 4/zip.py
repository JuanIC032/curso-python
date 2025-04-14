nombre = ['Ana', 'Hugo', 'Valeria']
edad = [65, 29, 42]

combinados = zip(nombre, edad) # Este resultado no es legible y hay que castearlo en una lista
print(combinados)

print('\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

nombre = ['Ana', 'Hugo', 'Valeria']
edad = [65, 29, 42]

combinados =list(zip(nombre, edad))
print(combinados)

print('\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

# zip solo llega al largo de la lista más corta, si la otra lista
# es mas larga, el excedente será ignorado
nombre = ['Ana', 'Hugo', 'Valeria']
edad = [65, 29, 42, 55]

combinados =list(zip(nombre, edad))
print(combinados)

print('\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

nombre = ['Ana', 'Hugo', 'Valeria']
edad = [65, 29, 42]
ciudad = ['Lima', 'Madrid', 'México']

combinados =list(zip(nombre, edad, ciudad))
print(combinados)

print('\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

for nombre,edad,ciudad in combinados:
    print(f'{nombre} tiene {edad} años y vive en {ciudad}')