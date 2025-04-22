class Pajaro:

    alas = True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print('pio, mi color es {}'.format(self.color))

    def volar(self, metros):
        print(f'El pájaro ha volado {metros} metros')
        self.piar() # Acceder a otros métodos

    def pintar_negro(self):
        self.color = 'negro' # Acceden y modifican atributos de objetos
        print(f'Ahora el pajaro es {self.color}')

    @classmethod
    def poner_huevos(cls, cantidad):
            print(f'Puso {cantidad} huevos')
            cls.alas = False  # Solo puede modificar atributos de clase

    @staticmethod
    def mirar():
        print('El pájaro mira')


piolin = Pajaro('amarillo', 'canario')

# Atributos de los métodos de instancia
piolin.pintar_negro()  # Acceden y modifican atributos de objetos
piolin.volar(50)  # Acceder a otros métodos
'''piolin.alas = False'''  # Modificar el estado de la clase
print(piolin.alas)

print('\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
# Métodos de clase

Pajaro.poner_huevos(3)
print(Pajaro.alas) # Solo puede modificar atributos de clase

print('\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
# Métodos estáticos
Pajaro.mirar() # No pueden acceder a los atributos de clase
piolin.mirar() # Tampoco a los atributos de instancia


class Personaje:

    def __init__(self, cantidad_flechas):
        self.cantidad_flechas = cantidad_flechas

    def lanzar_flecha(self):
        self.cantidad_flechas -= 1


Juan = Personaje(30)
Juan.lanzar_flecha()