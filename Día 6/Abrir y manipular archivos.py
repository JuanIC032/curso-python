mi_archivo = open('prueba.txt')

print(mi_archivo)

print('\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

print(mi_archivo.read())


print('\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

mi_archivo = open('prueba.txt')
una_linea = mi_archivo.readline()
print(una_linea.upper())

print('\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

una_linea = mi_archivo.readline()
print(una_linea)

una_linea = mi_archivo.readline()
print(una_linea)

print('\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
mi_archivo = open('prueba.txt')

for l in mi_archivo:
    print('Aquí dice: ' + l)

print('\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
mi_archivo = open('prueba.txt')

todas = mi_archivo.readlines()

todas = todas.pop()

print(todas)








