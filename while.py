'''contador = 0

while contador < 50:
    contador = contador + 1
    

    if contador == 4 :
        print('O 4 não sera mostrado')
        continue
    

    if contador >= 10 and contador <= 27:
        print('pulei todos')
        continue

    print(contador)

print('acabou')'''    

# while dentro de outro while

'''qnt_linha = 5 
qnt_coluna = 5

linha = 1
while linha <= qnt_linha:
    # sim, ai entra na validação da coluna
    coluna = 1
    while coluna <= qnt_coluna: # verifica primeiro o while interno ai dps que a coluna atingir 5, ai sim volta pra validação de linhas
        print(f'{linha=} {coluna=}')
        coluna += 1
    linha +=1        '''



frase = 'o python é uma linguagem de programação'

i = 0

while i < len(frase):
    letra_atual = frase[i]

    
    
    print(letra_atual)
    i += 1

