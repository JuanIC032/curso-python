def sumaejem(a,b):
    return a + b

print(sumaejem(5,6))

print('\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

def suma(*args):

    return sum(args)

print(suma(1,2,3,4,5,6))

print('\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

def suma_cuadrados(*args):
    total = 0
    for n in args:
        cuadrado = n**2
        total += cuadrado
    return total

print(suma_cuadrados(1,2,3))

print('\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

def suma_absolutos(*args):
    return sum(abs(arg) for arg in args)

print(suma_absolutos(1,2,3,-3,-2,-1))

print('\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

def numeros_persona(nombre, *args):
    return f'{nombre}, la suma de tus números es {sum(args)}'

print(numeros_persona('Federico', 75,20,65))