from random import *

# Lista inicial
palitos = ['-', '--','---','----']


# mezclar palitos
def mezclar(lista):
    shuffle(lista)
    return lista


# pedirle intento
def probar_suerte():
    intento = ''
    while intento not in ['1','2','3','4']:
        intento = input('Elije un número del 1 al 4: ')

    return int(intento)


# Comprobar intento
def chequear_intento(lista,intento):
    if lista[intento - 1] == '-':
        print('A lavar los platos')
    else:
        print('Esta vez te has salvado')

    print(f'Te ha tocado {lista[intento -1]}')

palitos_mezclados = mezclar(palitos)
seleccion = probar_suerte()
chequear_intento(palitos_mezclados,seleccion)


print('\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

def lanzar_dados():
    dado1 = randint(1,6)
    dado2 = randint(1,6)
    return dado1,dado2

def evaluar_jugada(dado1,dado2):
    suma_dados = dado1 + dado2
    mensaje = ''
    if suma_dados <= 6:
        mensaje = f'La suma de tus dados es {suma_dados}. ¡Lamentable!'
    elif 6 < suma_dados < 10:
        mensaje = f'La suma de tus dados es {suma_dados}. Tienes buenas chances'
    elif suma_dados >= 10:
        mensaje = f'La suma de tus dados es {suma_dados}. Parece una jugada ganadora'

    return mensaje

dado1, dado2 = lanzar_dados()
print(evaluar_jugada(dado1, dado2))

print('\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

def reducir_lista(lista):
    nueva_lista = set(lista)
    nueva_lista2 = list(nueva_lista)
    mayor = max(nueva_lista2)
    indicemayor = nueva_lista2.index(mayor)
    nueva_lista2.pop(indicemayor)
    return nueva_lista2

def promedio(lista):
    return sum(lista) / len(lista) if lista else 0

lista = reducir_lista([1,2,3,56,4,4,4,5,6])
prom = promedio(lista)
print(lista)
print(prom)


#optimizacion según chatgpt

'''def reducir_lista2(lista):
    nueva_lista = list(set(lista))  # Eliminar duplicados
    nueva_lista.remove(max(nueva_lista))  # Eliminar el número más alto
    return nueva_lista

print(reducir_lista([1, 2, 15, 7, 2]))  # [1, 2, 7]'''

print('\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

def lanzar_moneda():
    lanzada = choice(['Cara', 'Cruz'])
    return lanzada

def probar_suerte2(lanzada, lista_numeros):
    if lanzada == 'Cara':
        lista_numeros.clear()
        print('La lista se autodestruirá ')
        return lista_numeros
    elif lanzada == 'Cruz':
        print('La lista fue salvada ')
        return lista_numeros

lista_numeros = [1,2,3,4,5,6,7]
lanzada = lanzar_moneda()
print(probar_suerte2(lanzada,lista_numeros))