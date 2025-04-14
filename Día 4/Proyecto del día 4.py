from random import *

print('Hola, bienvenido al juego de \nadivinar el número\n')
nombre = input('¿Cómo te llamas? ')

print(f'\nBueno {nombre}, en este juego deberás adivinar \nun número del 1 al 100\n'
      f'y tienes 8 intentos')
print('\nComencemos')


numero_aleatorio = randint(1,101)
intentos = 8
intentos_fallidos = 1
while intentos >= 0:
    intento_adivi = int(input('Intenta adivinar el número: '))
    if intento_adivi <1 :
        print('No puedes usar ese numero, elige uno entre \nel 1 y el 100\n')
        intentos -= 1
        intentos_fallidos += 1
    elif intento_adivi >100 :
        print('No puedes usar ese numero, elige uno entre \nel 1 y el 100\n')
        intentos -= 1
        intentos_fallidos += 1
    elif intento_adivi == numero_aleatorio:
        print(f'\nGenial, has adivinado el numero en {intentos_fallidos} intentos')
        break
    elif intento_adivi > numero_aleatorio:
        print(f'\nIncorrecto, el número está más abajo,\nte quedan {intentos} intentos.\n')
        intentos -= 1
        intentos_fallidos +=1
        if intentos == 0:
            print('Te quedaste sin intentos, juega de nuevo')
            break
    elif intento_adivi < numero_aleatorio:
        print(f'\nIncorrecto, el número está más arriba,\nte quedan {intentos}.\n')
        intentos -= 1
        intentos_fallidos += 1
        if intentos == 0:
            print(f'Te quedaste sin intentos, el numero correcto \nera {numero_aleatorio}, \njuega de nuevo')
            break