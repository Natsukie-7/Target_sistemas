# Observe o trecho de codigo abaixo

# int INDICE = 13, SOMA = 0, K = 0

# ENQUANTO K < INDICE FAÇA
# {
#     K = K + 1
#     SOMA = SOMA + K
# }

# IMPRIMIR SOMA

# Em resumo, é so fazer a soma usando um loop.

indice, soma, k = 13, 0, 0

while k < indice:
    k += 1
    soma += k

print(soma)