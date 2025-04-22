from random import *
from os import *

class Persona():

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):

    def __init__(self, nombre, apellido, numero_cuenta, balance):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido} \nNúmero de cuenta: {self.numero_cuenta} \nBalance: ${self.balance}"

    def depositar(self):
        system('cls')
        deposito = int(input('Cuanto quieres depositar?\n '
                             '$'))
        self.balance += deposito
        print('\n✅ Depósito exitoso. Nuevo balance: ${}\n'.format(self.balance))

    def retirar(self):
        system('cls')
        while True:
            try:
                retiro = int(input('¿Cuánto quieres retirar?\n '
                                   '$'))
            except ValueError:
                print("❌ Ingresa un número válido.")
                continue

            if retiro > self.balance:
                print('❌ No tienes fondos suficientes para retirar esa cantidad.')
                print('💰 Balance actual: ${}'.format(self.balance))
                input("Presiona Enter para intentarlo de nuevo....")
            else:
                self.balance -= retiro
                print('\n✅ Retiro exitoso. Nuevo balance: ${}\n'.format(self.balance))
                break

def crear_cliente():

    system('cls')
    nombre = input("Nombre: ")
    apellido = input('Apellido: ')
    system('cls')
    numero_cuenta = randint(1000,999999)
    balance = 0
    print(f'Su cuenta ha sido creada con éxito! Bienvenido {nombre}!'
          f'\nSu número de cuenta es: {numero_cuenta}'
          f'\nSu balance es: ${balance}\n')

    input('Presiona enter para continuar...')

    return Cliente(nombre, apellido, numero_cuenta, balance)

def inicio():
    input('''Bienvenido a CagadaBank!!!
    
A continuación te pediremos una serie de datos para crear tu cuenta y puedas operar en breve

Presiona enter para continuar''')

    cliente = crear_cliente()


    while True:
        opcion = ''
        while opcion not in ['1','2']:
            system('cls')
            opcion = input('Bienvenido al menú principal, elige una de las siguientes opciones: '
                               '\n[1] - Depositar Dinero '
                               '\n[2] - Retirar Dinero\n')
        match opcion:
            case '1':
                cliente.depositar()

                fin_op = ''
                while fin_op not in ('y', 'n'):
                    fin_op = input('\nVolver al menú principal?  (y/n)\n')

                match fin_op:
                    case 'y':
                        system('cls')
                    case 'n':
                        system('cls')
                        break


            case '2':
                cliente.retirar()

                fin_op = ''
                while fin_op not in ('y', 'n'):
                    fin_op = input('\nVolver al menú principal?  (y/n)\n')

                match fin_op:
                    case 'y':
                        system('cls')
                    case 'n':
                        system('cls')
                        break

    print('Gracias por operar con nosotros!! '
          'Vuelva pronto!!')



inicio()