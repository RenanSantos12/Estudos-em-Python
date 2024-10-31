
# BOAS PRATICAS
'''velocidade = 61
local_carro = 102

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

velocidade_passou = velocidade > RADAR_1
carro_multado = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (local_carro + RADAR_RANGE)


if velocidade_passou:
    print('passou')

if carro_multado  and velocidade > RADAR_1:
    print('carro multado no radar 1')'''

# -------------------------------

# coNDIÇÔES

condicao = True
fazendo_algo = None

if condicao:
    fazendo_algo = True
    print('faça algo')

else:
    print('não passei')

if fazendo_algo is not None:
    print(condicao)    