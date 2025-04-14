from pathlib import Path

'''base = Path.home()
guia = Path(base, 'Europa','España',Path('Barcelona', 'Sagrada_Familia'))
# guia2 = guia.with_name('La_Pedrera.txt')
print(guia)
# print(guia2)
print(guia.parent.parent)'''

'''guia = Path(Path.home(),'Europa')

for txt in Path(guia).glob('**/*.txt'):
    print(txt)'''

'''guia = Path('Europa', 'España', 'Barcelona', 'Sagrada_familia.txt')
en_europa = guia.relative_to(Path('Europa'))
en_espania = guia.relative_to(Path('Europa', 'España'))
print(en_europa)
print(en_espania)'''

from pathlib import Path
"""
# Obtener todos los métodos de Path
funciones = [func for func in dir(Path) if not func.startswith("_")]

numeracion = range(1,101)

lista_combinada = [item for pair in zip(numeracion, funciones) for item in pair]

print(lista_combinada)


print(f"Pathlib tiene {len(funciones)} funciones:")
for f in lista_combinada:
    print(f'{f}\n')"""

ruta_inicial = Path('C:/Users/jucei/Recetas')
contador = 0
for direc in ruta_inicial.iterdir():
    contador += 1
    directorios = Path(direc).name
    print(f'[{contador}] - {directorios}')