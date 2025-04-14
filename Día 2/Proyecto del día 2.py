nombre = input('Nombre del vendedor: ')
monto = input('Monto de sus ventas: ')
comision= round(int(monto) * 13 / 100, 2 )
print(f'Felicitaciones {nombre}!, en total has \nganado ${comision} en comisión de tus ventas')