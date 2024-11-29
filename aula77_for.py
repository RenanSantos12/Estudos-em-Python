'''digitacao = 'Renan lindo'

for caracter in digitacao:
    print(caracter)

    '''

palavra_secreta = 'perfume'
letras_acertadas = ''
while True:
    letra_digitada = input('Digite uma letra: ')

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letras_acertadas

        
