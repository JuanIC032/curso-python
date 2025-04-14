from os import makedirs
from pathlib import Path
import os

'''ruta = os.getcwd()
print(ruta)'''

'''ruta = os.chdir('C:\\Users\\jucei\\OneDrive\\Documentos\\alternativo')
archivo = open('archivo.txt')
print(archivo.read())'''

ruta = makedirs('C:\\Users\\jucei\\OneDrive\\Documentos\\alternativo\\otra')

# ruta = 'C:\\Users\\jucei\\PycharmProjects\\PythonProject16días\\Día 6\\Prueba.txt'

# elemento = os.path.basename(ruta) devuelve el nombre del archivo
# elemento = os.path.dirname(ruta) devuelve el ultimo directorio
# elemento = os.path.split(ruta) devuelve un tuple con el directorio y la base

# os.rmdir('C:\\Users\\jucei\\OneDrive\\Documentos\\alternativo\\otra')

# otro_archivo = open('C:\\Users\\jucei\\OneDrive\\Documentos\\alternativo\\archivo.txt')
# print(otro_archivo.read())

'''carpeta = Path('/Users/jucei/OneDrive/Documentos/alternativo')
archivo = carpeta / 'archivo.txt'

mi_archivo = open(archivo)
print(mi_archivo.read())'''