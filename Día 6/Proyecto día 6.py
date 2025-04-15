import os
from pathlib import *
from os import system, makedirs


def inicio():

    ruta_inicial = Path('C:/Users/jucei/Recetas')

    print(f'''Bienvenido al recetario, hay un montón de recetas a 
las que podrás acceder a través de un menú que será
mostrado en instantes.
    
La ruta inicial es {ruta_inicial}\n''')

    continuacion = ''

    while continuacion not in ('y','n'):
        continuacion = input('Continuar? (y/n)')

    if continuacion == 'n':
        pass
    return ruta_inicial

def total_recetas(ruta_inicial):
    contador = 0

    for txt in Path(ruta_inicial).glob('**/*.txt'):
        contador += 1

    print(f'''La cantidad de recetas que hay 
en todo el recetario es: \n
{contador} recetas encontradas''')

    continuacion = ''
    while continuacion not in ('y', 'n'):
        continuacion = input('Continuar al menú principal? (y/n)')

def menu_principal():
    system('cls')
    opcion = ''

    while opcion not in ('1','2','3','4','5','6'):
        opcion = input('''Bienvenido al menú principal, elige una de las
siguientes opciones:
[1] - Leer receta
[2] - Crear receta
[3] - Crear categoría
[4] - Eliminar receta
[5] - Eliminar categoría
[6] - Finalizar programa

''')
        system('cls')

    return opcion

def elegir_categoria(ruta_inicial):

    system('cls')
    contador = 0
    directorios1 = []

    print('Elige una de las siguientes categorías: \n')

    for direc in ruta_inicial.iterdir():

        if direc.is_dir():

            directorios1.append(direc)
            contador += 1
            print(f'''[{contador}] - {direc.name}''')

    if not directorios1:
        print('No hay categorías disponibles')
        return None

    eleccion = 0
    while int(eleccion) not in range(1,contador+1):
        try:
            eleccion = int(input('\nElección: '))
        except ValueError:
            print("Por favor, ingresa un número válido.")

    ruta_cat = directorios1[eleccion-1]

    return ruta_cat

def elegir_receta(ruta_cat):
    system('cls')
    contador = 0
    recetas = []

    print('Elige una de las siguientes recetas: \n')

    for rece in ruta_cat.iterdir():
        recetas.append(rece)
        contador += 1
        print(f'[{contador}] - {rece.stem}')

    if not recetas:
        print('No hay recetas disponibles')
        return None

    eleccion = 0
    while int(eleccion) not in range(1, contador+1):

        try:
            eleccion = int(input('\nElección: '))

        except ValueError:
            print("Por favor, ingresa un número válido.")

    rece_escogida = recetas[eleccion-1]

    return rece_escogida

def opcion1(ruta_inicial):
    ruta_cat = elegir_categoria(ruta_inicial)
    system('cls')
    receta_eleg = elegir_receta(ruta_cat)
    system('cls')
    receta_abierta = open(receta_eleg)
    print(receta_abierta.read())
    receta_abierta.close()

    fin_op = ''
    while fin_op not in ('y', 'n'):
        fin_op = input('\nVolver al menú principal?  (y/n)\n')

    match fin_op:
        case 'y':
            system('cls')
            return False

        case 'n':
            system('cls')
            return True

def opcion2(ruta_inicial):
    ruta_cat = elegir_categoria(ruta_inicial)
    system('cls')

    nombre_archivo = ''
    while not nombre_archivo not in str():
        nombre_archivo = input('Cómo se llamará el archivo: ')

    creacion_archivo = ruta_cat /  f'{nombre_archivo}.txt'

    if creacion_archivo.exists():
        print("⚠️ Ya existe un archivo con ese nombre.\n")
        fin_op = ''
        while fin_op not in ('y', 'n'):
            fin_op = input('\nVolver al menú principal?  (y/n)\n')

        match fin_op:
            case 'y':
                system('cls')
                return False
            case 'n':
                system('cls')
                return True

    abrir_archivo = open(creacion_archivo, 'w')
    abrir_archivo.write(input('Escribe la receta: \n'))

    fin_op = ''
    while fin_op not in ('y', 'n'):
        fin_op = input('\nVolver al menú principal?  (y/n)\n')

    match fin_op:
        case 'y':
            system('cls')
            return False
        case 'n':
            system('cls')
            return True

def opcion3(ruta_inicial):
    nombre_cat = input('Cómo se llamará la categoría: \n')
    system('cls')
    makedirs( ruta_inicial / nombre_cat)
    print('La categoría fue creada exitosamente')

    fin_op = ''
    while fin_op not in ('y', 'n'):
        fin_op = input('\nVolver al menú principal?  (y/n)\n')

    match fin_op:
        case 'y':
            system('cls')
            return False
        case 'n':
            system('cls')
            return True

def opcion4(ruta_inicial):
    ruta_cat = elegir_categoria(ruta_inicial)
    system('cls')
    ruta_rece = elegir_receta(ruta_cat)
    system('cls')
    ruta_rece.unlink()
    print('El archivo fue eliminado exitosamente        ')

    fin_op = ''
    while fin_op not in ('y', 'n'):
        fin_op = input('\nVolver al menú principal?  (y/n)\n')

    match fin_op:
        case 'y':
            system('cls')
            return False
        case 'n':
            system('cls')
            return True

def opcion5(ruta_inicial):
    ruta_cat = elegir_categoria(ruta_inicial)
    system('cls')
    errorelim = False
    try:
        os.rmdir(ruta_cat)
    except OSError:
        print("❌ No se puede eliminar la categoría: no está vacía.")
        errorelim = True

    match errorelim:
        case False:
            print('La categoría fue eliminada exitosamente')


    fin_op = ''
    while fin_op not in ('y', 'n'):
        fin_op = input('\nVolver al menú principal?  (y/n)\n')

    match fin_op:
        case 'y':
            system('cls')
            return False
        case 'n':
            system('cls')
            return True

def opcion6():
    return True

def men_prin_compl(ruta_inicial, opcion):
    match opcion:
        case 1:
            return opcion1(ruta_inicial)
        case 2:
            return opcion2(ruta_inicial)
        case 3:
            return opcion3(ruta_inicial)
        case 4:
            return opcion4(ruta_inicial)
        case 5:
            return opcion5(ruta_inicial)
        case 6:
            return opcion6()


ruta_inicial = inicio()
system('cls')
total_recetas(ruta_inicial)
system('cls')
fin = False
while fin == False:
    opcion = menu_principal()
    system('cls')
    fin = men_prin_compl(ruta_inicial, int(opcion))
