texto = input('Ingrese su texto: ')
txtmin = texto.lower()
letras = [input('Primera letra: ').lower(), input('Segunda letra: ').lower(), input('Tercera letra: ').lower()]


conteoletras = [txtmin.count(letras[0]), txtmin.count(letras[1]), txtmin.count(letras[2])]
print(f' La letra \'{letras[0]}\' aparece {conteoletras[0]} veces\n',
      f' La letra \'{letras[1]}\' aparece {conteoletras[1]} veces\n',
      f' La letra \'{letras[2]}\' aparece {conteoletras[2]} veces\n')


texto_total = texto.split()
print(f'En total hay {len(texto_total)} palabras en el texto')

print(f'\nLa primera letra del texto es {texto[0]}\n',f'La última letra del texto es {texto[-1]}\n')

txtreves = texto.split()
txtreves.reverse()
txtreves = ' '.join(txtreves)
print(f'Texto en reversa:\n {txtreves}')

palabrabusq = input('\nIntroduce la palabra a buscar: ')
busq = palabrabusq in texto
respuesta = {'r1':f'La palabra \'{palabrabusq}\' no se encuentra en el texto',
             'r2':f'La palabra \'{palabrabusq}\' se encuentra en el texto'}

if busq is True :print(respuesta['r2'])
if busq is False :print(respuesta['r1'])