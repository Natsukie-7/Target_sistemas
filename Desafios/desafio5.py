# 5) Escreva um programa que inverta os caracteres de um string.

# IMPORTANTE:
# a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente 
# definida no código;
# b) Evite usar funções prontas, como, por exemplo, reverse;

# Então eu tenho de criar na unha esse reversso, DESAFIO ACEITO

def isolar_letras(palavra):
    lista = []
    for letra in palavra:
        lista.append(letra)

    return lista

def inverter(lista_letras):
    invertido = []
    for letra in range(1, len(lista_letras) + 1):
        invertido.append(lista_letras[-letra])

    
    return ''.join(invertido)
    
palavra = input('Me fale uma palavra para eu inverter: ')

letras_isoladas = isolar_letras(palavra)
print(inverter(letras_isoladas))


