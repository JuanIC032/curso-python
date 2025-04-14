def check_3_cifras(numero):
    return numero in range(100,1000)

resultado = check_3_cifras(658)
print(resultado)

print('\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

def check_3_cifras(numero):
    return numero in range(100,1000)

suma = 120 +345

resultado = check_3_cifras(suma)
print(resultado)

print('\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

def check_3_cifras(lista):
    lista_3_cifras = []
    for n in lista:
        if n in range(100,1000):
            lista_3_cifras.append(n)
        else:
            pass
    return lista_3_cifras

resultado = check_3_cifras([555,99,600])
print(resultado)

print('\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

lista_numeros = [0,1,2,3,4,5,6]
def todos_positivos(lista_numeros):
    for n in lista_numeros:
        if n >= 0:
            pass
        else:
            return False
    return True

print(todos_positivos([0,1,2,3,4,5,6]))

print('\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')


def suma_menores(lista_numeros):
    suma = 0
    for numero in lista_numeros:
        if numero in range(1, 1000):
            suma += numero
        else:
            pass
    return suma

print(suma_menores([-5,3777,34,65,456,1039,-45]))

print('\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

def cantidad_pares(lista_numeros):
    conteo = 0
    for n in lista_numeros:
        if n%2 == 0:
            conteo += 1
        else:
            pass
    return conteo

resultado = cantidad_pares([1,2,3,4,6,8,10,12,222,220,110,100,5,6,7,8,9,10])
print(resultado)
