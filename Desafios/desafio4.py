# 4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:

# SP – R$67.836,43
# RJ – R$36.678,66
# MG – R$29.229,88
# ES – R$27.165,48
# Outros – R$19.849,53

# Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado
# teve dentro do valor total mensal da distribuidora.

import json

def calcular_faturamento_total(faturamento):
    faturamento_total = 0
    for estado in faturamento:
        faturamento_total += faturamento[estado]

    return faturamento_total


def calcular_porcentagem_dos_estados(faturamento):
    representacao = []
    for estado in faturamento:
        valor = faturamento[estado]
        porcentagem = (valor * 100) / calcular_faturamento_total(faturamento)
        representacao.append(porcentagem)

    return representacao


with open(r'Target_sistemas/Desafios/faturamento_estados.json', 'r') as distribuidora:
    faturamentos = json.load(distribuidora)

porcetagem_de_cada_estado = calcular_porcentagem_dos_estados(faturamentos)
print('Aqui esta a porcetagem de cada estado\n')
for estado, porcetagem in zip(faturamentos, porcetagem_de_cada_estado):
    print(f'{estado}: {porcetagem:.2f}%')
    



    