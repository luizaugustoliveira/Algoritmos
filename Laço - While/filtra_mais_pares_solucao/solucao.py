# UFCG
# Prog1
# Luiz Augusto Oliveira de Farias
# Matrícula: 120110389
# Questão: Filtra com mais pares

def conta_par(seq):
    pares = 0
    for i in range(len(seq)):
        if seq[i] % 2 == 0:
            pares += 1
    return pares

def conta_impar(seq):
    impares = 0
    for i in range(len(seq)):
        if seq[i] % 2 == 1:
            impares += 1
    return impares

def separa_por_espacos(entrada):
    tokens = entrada.split()
    numeros = []
    for tk in tokens:
        numeros.append(int(tk))
    return numeros

def linhas_filtradas(seq):
    linhas = []
    for i in range(len(seq)):
        impares = conta_impar(seq[i])
        pares = conta_par(seq[i])
        if pares > impares:
            linhas.append(seq[i])
    return linhas

def imprime(seq):
    saida = ""
    for i in range(len(seq)):
        num = seq[i]
        if i == len(seq) - 1:
            saida += f"{num}"
        else:
            saida += f"{num} "
    return saida

sequencias = []
while True:
    entrada = input()
    if entrada == "fim": break
    sequencias.append(separa_por_espacos(entrada))
    
sequencias_validas = linhas_filtradas(sequencias)
print(f"filtradas: {len(sequencias_validas)}")

if sequencias != []: 
    for i in range(len(sequencias_validas)):
        print(imprime(sequencias_validas[i]))
    
# Sugestão para melhorar o programa:
#   Coloca todas as linhas em forma de lista dentro de uma lista maior
#   se a quantidade de elementos das linhas dividido por 2 ou mais que isso for par, essas linhas precisarão estar na saída
#   a função conta_par, conta_impar, separa_por espaços e imprime não precisa
#   posso imprimir a linha do jeito que tá lá sem precisar converter pra inteiro primeiro  