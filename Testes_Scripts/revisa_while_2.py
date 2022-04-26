# Problema pra analisar quais listas possuem mais elementos 

# 2 3 4 5 6 
# 3 2 1
# 5 7 9
# fim

# Sequencia 1: 2 3 4 5 6 

maior = 0 # maior tamanho da sequencia 
sequencia = "" # sequência
posicao = 0 # posição da sequência
contador = 0

while True:

    entrada = input()

    if entrada == "fim": break

    contador += 1
    numeros = entrada.split()

    if len(numeros) > maior:
        maior = len(numeros)
        sequencia = entrada
        posicao = contador

if contador != 0:
    print(f"Sequência {posicao}: {sequencia}")