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

qnt_linha = 5 
qnt_coluna = 5

linha = 1
while linha <= qnt_linha:
    coluna = 1
    while coluna <= qnt_coluna:
        print(f'{linha=} {coluna=}')
        coluna += 1
    linha +=1        