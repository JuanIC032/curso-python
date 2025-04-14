def suma(**kwargs):
    print(type(kwargs))

suma(x=3,y=5,z=2)

print('\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

def suma(**kwargs):
    for clave,valor in kwargs.items():
        print(f'{clave} = {valor}')

suma(x=3,y=5,z=2)

print('\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

def suma(**kwargs):
    total = 0
    for clave,valor in kwargs.items():
        print(f'{clave} = {valor}')
        total += valor
    return total

print(suma(x=3,y=5,z=2))

print('\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

def prueba(num1,num2,*args,**kwargs):
    print(f'El primer valor es {num1}')
    print(f'El segundo valor es {num2}')

    for arg in args:
        print(f'arg = {arg}')


    for clave,valor in kwargs.items():
        print(f'{clave} = {valor}')

prueba(15,50,100,200,300,400, x='uno', y='dos', z='tres')

print('\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

def prueba(num1,num2,*args,**kwargs):
    print(f'El primer valor es {num1}')
    print(f'El segundo valor es {num2}')

    for arg in args:
        print(f'arg = {arg}')


    for clave,valor in kwargs.items():
        print(f'{clave} = {valor}')


args = [100,200,300,400]
kwargs = {'x':'uno','y':'dos','z':'tres'}


prueba(15,50, *args, **kwargs)

print('\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

def cantidad_atributos(**kwargs):
    cantidad = 0
    for clave in kwargs.items():
        cantidad += 1
    return cantidad
print(cantidad_atributos(x=10,v=12,l=23))

print('\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

def lista_atributos(**kwargs):
    lista = []
    for valor in kwargs.values():
        lista.append(valor)
    return lista

print(lista_atributos(x=1,z=2,y=3))

print('\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

def describir_persona(nombre,**kwargs):
    print(f'Características de {nombre}: \n')
    for clave,valor in kwargs.items():
        print(f'{clave}: {valor}')

caracteristicas = {'Color de ojos': 'Marrón', 'Raza':'Pardo', 'Contextura':'Robusto'    }
describir_persona('Juan', **caracteristicas )