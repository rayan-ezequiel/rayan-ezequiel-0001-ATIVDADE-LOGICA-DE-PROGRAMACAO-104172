import os
os.system('cls')

# Em uma loja de CD's existem apenas quatro tipos de preços que estão associados a cores. '
# 'Assim, os CD's que ficam na loja não são marcados por preços e sim por cores.
# Desenvolva um algoritmo que, a partir da entrada da cor, o software mostre o preço.
# A loja está atualmente com a seguinte tabela de preços:
# verde = 10
# azul = 20
# amarelo = 30
# vermlho = 40

print('Loja de CDs')
cor = input('Digite a cor que você deseja: ').lower()

match cor:
    case 'vermelho':
        print('o Preço é R$ 40,00.')
    case 'amarelo':
        print('O Preço é R$ 30,00.')
    case 'azul':
        print('O Preço é R$ 20,00.')
    case 'verde':
        print('O Preço é R$ 10,00.')
    case _:
        print('Opcção inválida.')