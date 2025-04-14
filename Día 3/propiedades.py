#Los strings son inmutables, no se pueden modificar, este es el ejemplo:
nombre = 'Carina'
#nombre[0] = 'K'
print(nombre)

#los strings son concatenables
n1 = 'Kari'
n2 = 'na'
print(n1+n2)

# también son multiplicables
print(n1* 10)

# usando tres comillas dobles o simples podemos tener saltos de línea sin usar \n
poema = '''Mil pequeños peces blancos
como si hirviera
el color del agua'''
print(poema)

# usando 'in' o 'not in' podemos saber si hay algun caracter dentro de un string
print('agua' in poema)
print('sol' not in poema)

# 'len' sirve para saber cuantos caracteres hay en total en un string
print(len(poema))