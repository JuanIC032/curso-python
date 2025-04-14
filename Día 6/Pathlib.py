from pathlib import Path, PureWindowsPath

carpeta = Path("C:/Users/jucei/PycharmProjects/PythonProject16días/Día 6/Prueba.txt")

ruta_windows = PureWindowsPath(carpeta)
print(ruta_windows)

# print(carpeta.read_text())
# print(carpeta.name)
# print(carpeta.suffix)
# print(carpeta.stem)

if not carpeta.exists():
    print('Este archivo no existe')
else:
    print('Genial, existe')
