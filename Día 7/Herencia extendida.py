# La clase hija tiene 3 tipos de métodos:
# 1 los métodos heredados exactamente iguales a la clase padre
# 2 Los métodos herdados pero modificados luego
# 3 Los métodos totalmente nuevos que no tenia en la clase padre
# tambien una clase puede heredar de otras clases y hasta entre generaciones de clases

class Animal:

    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print('Este animal ha nacido')

    def hablar(self):
        print('Este animal emite un sonido')


class Pajaro(Animal):

    def __init__(self,edad,color, altura_vuelo):
        super().__init__(edad,color)
        self.altura_vuelo = altura_vuelo

    def hablar(self):   # 2)_ Método heredado pero modificado luego
        print('pio')

    def volar(self, metros):  # 3 Método totalmente nuevo que no tenia en la clase padre
        print(f'El pajaro vuela {metros} metros')

piolin = Pajaro(3, 'amarillo', 60)

mi_animal = Animal(5, 'negro')



piolin.nacer() # 1 Método heredado exactamente igual a la clase padre
piolin.hablar() # 2 Método heredado pero modificado luego
piolin.volar(100) # 3 Método totalmente nuevo que no tenia en la clase padre

print('\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

class Padre:
    def hablar(self):
        print('Hola')

class Madre:
    def reir(self):
        print('ja ja')

    def hablar(self):
        print('que tal')

class Hijo(Padre, Madre):
    pass

class Nieto(Hijo):
    pass

mi_nieto = Nieto()
mi_nieto.reir()
mi_nieto.hablar()


print(Nieto.__mro__)



















