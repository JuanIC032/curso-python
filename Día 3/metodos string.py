texto = 'Este es el texto de Federico'

resultado = texto

print(resultado)

# Con '.upper' podemos hacer mayuscula un string completo o algunos caracteres o palabras si lo indicamos
texto = 'Este es el texto de Federico'

resultado = texto.upper()

print(resultado)

# En este ejemplo le indico a upper que letra hacer mayuscula, al hacer print solo mostrará 'T'
texto = 'Este es el texto de Federico'

resultado = texto[2].upper()

print(resultado)

# 'lower' es lo contrario a 'upper' pero funciona de la misma manera
texto = 'Este es el texto de Federico'

resultado = texto.lower()

print(resultado)

# '.split' divide el string dependiendo de que coloquemos como factor, en este caso un espacio ()
texto = 'Este es el texto de Federico'

resultado = texto.split( )

print(resultado)

# En este ejemplo en el factor coloqué una t ('t'), entoces el string se va a dividir/cortar cada vez que haya una 't'
texto = 'Este es el texto de Federico'

resultado = texto.split('t')

print(resultado)

# '.join' se usa para unir listas de strings, las comillas del principio determinan con que se van a unir los objetos.
# este caso se usa el espacio, los strings se uniran pero estaran 'separados' por espacios
a = 'Aprender'
b = 'Python'
c = 'es'
d = 'genial'
e = ' '.join([a,b,c,d])
print(e)

# en este caso los strings se unirán y estarán separados por una barra '-'
a = 'Aprender'
b = 'Python'
c = 'es'
d = 'genial'
e = '-'.join([a,b,c,d])
print(e)

# '.find' se usa para buscar un caracter y devuelve su posición numérica, es casi igual a '.index'
texto = 'Este es el texto de Federico'

resultado = texto.find('s')

print(resultado)

# '.replace' se utiliza para remplazar un caracter o varios en un string, el primer factor es el objetivo que se va a
# modificar y el segundo factor son el/los caracteres por los que se va a reemplazar el objetivo
texto = 'Este es el texto de Federico'

resultado = texto.replace('Federico', 'todos')

print(resultado)

# varios .replace consecutivos
texto = 'Mi moto alpina derrapante '

resultado = texto.replace('a', 'e').replace('i', 'e').replace('o', 'e')

print(resultado)