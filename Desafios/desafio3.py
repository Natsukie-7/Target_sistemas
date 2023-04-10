# 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem 
# que desejar, que calcule e retorne:

# • O menor valor de faturamento ocorrido em um dia do mês;
# • O maior valor de faturamento ocorrido em um dia do mês;
# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

# IMPORTANTE:
# a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
# b) Podem existir dias sem faturamento, como nos finais de semana e feriados. 
# Estes dias devem ser ignorados no cálculo da média;

import json
 
with open(r'Target_sistemas/Desafios/faturamento.json', 'r') as arquivo_faturamento: # leitura do arquivo json contendo o faturamento diário
    faturamento_diario = json.load(arquivo_faturamento)

# cálculo do menor e do maior valor de faturamento ocorrido em um dia do mês
menor_faturamento = min(faturamento_diario)
maior_faturamento = max(faturamento_diario)

def mediaMensal(arquivo): # cálculo da média mensal de faturamento, ignorando os dias sem faturamento
    dias_com_faturamento = []
    for faturamento in faturamento_diario:
        faturamento = int(faturamento)
        if faturamento > 0:
            dias_com_faturamento.append(faturamento)

    return sum(dias_com_faturamento) / len(dias_com_faturamento)

# contagem do número de dias em que o valor de faturamento diário foi superior à média mensal
dias_acima_da_media = 0
for faturamento in faturamento_diario:
    faturamento = int(faturamento)
    if faturamento > mediaMensal(arquivo_faturamento):
        dias_acima_da_media += 1

# exibição dos resultados
print(f'''
Menor faturamento: {menor_faturamento}
Maior faturamento: {maior_faturamento}
Número de dias com faturamento acima da média mensal: {dias_acima_da_media}
''')