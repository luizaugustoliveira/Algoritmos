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

def listas(seq):
    listas = []
    for i in range(len(seq)):
        impares = conta_impar(seq[i])
        pares = conta_par(seq[i])
        if pares > impares:
            listas.append(seq[i])
    return listas

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
    linhas = separa_por_espacos(entrada)
    sequencias.append(linhas)
    sequencias_validas = listas(sequencias)

print(f"filtradas: {len(sequencias_validas)}")

for i in range(len(sequencias_validas)):
    print(imprime(sequencias_validas[i]))
    