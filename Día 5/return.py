def multiplicar(num1,num2):
    return num1 * num2

resultado = (multiplicar(5,10))
print(resultado)

def invertir_palabra(palabra):
    palabra = palabra[::-1]
    palabra = palabra.upper()
    return palabra

print(invertir_palabra('Python'))