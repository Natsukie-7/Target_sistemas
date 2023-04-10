# # 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores 
# anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado 
# um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a
# sequência.

# IMPORTANTE:
# Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser 
# previamente definido no código;

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

def fibonacci(numero_a_verificar): # essa função ira me gerar a sequencia de fibonacci
    lista_fibonacci = [0, 1]

    for i in range(1, numero_a_verificar):         
        posicao_anterior = lista_fibonacci[-2]
        Valor_Atual_DA_Sequencia = lista_fibonacci[-1] 
        nova_sequencia = posicao_anterior + Valor_Atual_DA_Sequencia
        lista_fibonacci.append(nova_sequencia)

    return lista_fibonacci

        
def verifique_na_lista(numero_a_verificar): # essa ira verificar se o numero esta ou não na lista
    validacao = numero_a_verificar in fibonacci(numero_a_verificar)

    return f"O valor {numero_a_verificar} esta na lista de fibonacci, na  {fibonacci(numero_a_verificar).index(numero_a_verificar) + 1}º posição" if validacao == True else f"O valor {numero_a_verificar} não faz parte da sequencia"


def main():
    while True:    
        valor = input('Qual o valor gostaria de verificar: ')
        if valor != '':
            print(verifique_na_lista(int(valor)))
        
        else:
            break
    

main()