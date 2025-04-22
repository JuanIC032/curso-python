class Vaca:

    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + ' dice muuu')


class Oveja:

    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + ' dice beee')

vaca1 = Vaca('Aurora')
oveja1 = Oveja('Nube')

vaca1.hablar()
oveja1.hablar()

print('\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

animales = [vaca1, oveja1]

for animal in animales:
    animal.hablar()

print('\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

def animal_habla(animal):
    animal.hablar()


animal_habla(vaca1)
animal_habla(oveja1)

print('\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')


palabra = "polimorfismo"
lista = ["Clases", "POO", "Polimorfismo"]
tupla = (1, 2, 3, 80)


lista = [palabra, lista, tupla]

for iten in lista:
    print(len(iten))














