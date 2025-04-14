mi_texto = 'Esta es una prueba'
resultado = mi_texto[-4]
print(resultado)

resultado = mi_texto.index('a')
print(resultado)

#index es sensible a las mayúsculas
resultado = mi_texto.index('prueba')
print(resultado)

#Index solo busca de izquierda a derecha hasta encontrar el string que busca

#El segundo parámetro de index permite decirle a python desde donde comenzar a buscar
resultado = mi_texto.index('a', 5)
print(resultado)

#También se le puede colocar un limite de busqueda en el tercer parámetro (si
# colocamos el numero 10, solo buscara hasta el nueve, el numero limite no esta incluido
resultado = mi_texto.index('a', 0, 10)
print(resultado)

#También tenemos la función .rindex que lo que hace es buscar de derecha a izquierda
resultado = mi_texto.rindex('a')
print(resultado)