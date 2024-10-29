# TODO condição algoritimos 

#primeiro = input('Digite o primeiro numero : ')
#segundo = input('Digite o segundo numero : ')
#
#if primeiro >= segundo:
#    print('numero maior é', primeiro, 'e o menor é', segundo)
#    
#else:
#    print('o numero maior é', segundo, 'e o menor é', primeiro)
 
# -------------------------------------------------

entrada = input(f'[E]ntar [S]air :')
senha = input('senha :')
senha_acesso = '4022'

if entrada == 'E' or 'e' and senha == senha_acesso:
    print('entre')

else:
    print('Sair !!')    

# -------------------------------------------------

# not in

nome = input('Digite seu nome :')
encontrar = input('digite o que deseja encontrar :')

if encontrar in nome:
    print(f'{encontrar} esta em {nome}')

else:
    print('erro')    