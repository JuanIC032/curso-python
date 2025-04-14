# and or not
# usando and los dos
mi_bool = 4 < 5 and 5 > 6
print(mi_bool)

mi_bool = (4 < 5) and (5 == 2+3) # para una mayor legilibilidad ponemos cada operacion entre parentesis
print(mi_bool)

mi_bool = (55 == 55) and ('perro' == 'perro')
print(mi_bool)

mi_bool = 10 == 10 or 3 == 3
print(mi_bool)

mi_bool = 1 == 10 or 3 == 3
print(mi_bool)

mi_bool = 1 == 10 or 3 == 30
print(mi_bool)

texto = 'esta frase es breve'

mi_bool = ('frase' in texto) and ('pyhon' in texto)
print(mi_bool)

mi_bool = not 'a' == 'a'