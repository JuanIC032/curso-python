archivo = open('prueba.txt','a')
archivo.write('Bienvenido')
archivo.close()

# Hay tres opciones para colocar en el segundo argumento de open, la primera
# es 'r' que solo permite la lectura del archivo, la segunda es 'w' que permite
# la escritura, si el nombre del archivo no existe entonces se creará uno, si
# ya existe se sobrescribirá y se perderá lo anterior en el archivo.
# la tercera opción es 'a' que lo que hace es colocar el cursor al
# final del archivo, manteniendo el contenido original y empezando a escribir
# desde el final