# Ejercicio 1

def devolver_distintos(num1,num2,num3):
    nums = [num1,num2,num3]
    suma = sum(nums)
    if suma > 15:
        return max(nums)
    elif suma < 10:
        return min(nums)
    elif 10< suma <15:
        nums.remove(max(nums))
        nums.remove(min(nums))
        return max(nums)

# corrción del profe
#else:
#lista.sort()
#return lista[1]

print(devolver_distintos(8,2,3))

print('\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

# Ejercicio 2

def ordena_letras(palabra):
    letras = list(set((palabra).lower()))
    letras.sort()
    return letras

print(ordena_letras('cascarrabias'))

print('\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
# Ejercicio 3

def doble_cero(*args):
    lista = list(args)
    string = ''.join(str(num) for num in lista)
    prueba_logica = string.find('00')
    if prueba_logica != -1:
        return True
    elif prueba_logica == -1:
        return False


print(doble_cero(1,2,3,4,5,6,7,8,0,6,9,0,6,0,9,0,0))

print('\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

# Correccion de chatgpt

def doble_cero(*args):
    for i in range(1, len(args)):  # Empieza desde el segundo elemento
        if args[i] == 0 and args[i-1] == 0:  # Revisa si dos ceros consecutivos
            return True
    return False

# Prueba
print(doble_cero(1, 2, 3, 4, 5, 6, 7, 8, 0, 6, 9, 0, 6, 0, 9, 0, 0))  # True
print(doble_cero(6, 0, 5, 1, 0, 3, 0, 1))  # False

#como hizo el profe
def ceros_vecinos(*args):

    contador = 0

    for num in args:

        if contador + 1 == len(args):
            return False
        elif args[contador] == 0 and args[contador +1] == 0:
            return True
        else:
            contador +=1
    return False



print('\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

# Ejercicio 4, se lo copie al profe

def contar_primos(numero):
    lista_primos = [2]
    iteracion = 3
    if numero < 2:
        return 0
    while iteracion <= numero:

        for n in range(3,iteracion,2):
            if iteracion % n == 0:
                iteracion +=2
                break
        else:
            lista_primos.append(iteracion)
            iteracion += 2
    print(lista_primos)
    return len(lista_primos)

print(contar_primos(50))
