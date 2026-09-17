import os
os.system('cls')

# Escreva um algoritmo que leia o número de litros vendidos e o tipo de combustível
# (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor
# a ser pago pelo cliente, sabendo-se
# que o preço do litro da gasolina é R$ 6,59 e o preço do litro do álcool é R$ 3,79.

# Álcool 	Até 25 litros 	10%
# Álcool 	Acima de 25 litros 	20%
# Gasolina 	Até 25 litros 	15%
# Gasolina 	Acima de 25 litros 	30%

litros = float(input('Quantos litros você deseja ? '))
print('A-álcool') # R$ 3,79.
print('G-gasolina') # R$ 6,59
tipo = input('Qual tipo você deseja: ').upper()

if tipo == 'A':
    A = litros * 3.79
    if litros <= 25:
        valor = A * 0.10
        print(f'Valor a ser pago: R$ {A:.2f}')
        print(f'Valor a ser pago com desconto: R$ {A - valor:.2f}')
    elif litros > 25:
        valor = A * 0.20
        print(f'Valor a ser pago: R$ {A:.2f}')
        print(f'Valor a ser pago com desconto: R$ {A - valor:.2f}')

if tipo == 'G':
    G = litros * 6.59
    if litros <= 25:
        valor = G * 0.15
        print(f'Valor a ser pago: R$ {G:.2f}')
        print(f'Valor a ser pago com desconto: R$ {G - valor:.2f}')
    elif litros > 25:
        valor = G * 0.30
        print(f'Valor a ser pago sem desconto: R$ {G:.2f}')
        print(f'Valor a ser pago com desconto: R$ {G - valor:.2f}')
