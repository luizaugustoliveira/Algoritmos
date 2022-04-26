# UFCG
# Prog1
# Luiz Augusto Oliveira de Farias
# Matrícula: 120110389
# Questão: Inversos das Potências de 2 - Série Convergente

limite = float(input())

alvo = 2/3 
soma = 0
expoente = 0
while True:
    if abs(alvo - soma) > limite:
        print(f"{soma:.14f}")
        expoente += 1
        if expoente % 2 == 0:
            soma = abs(soma + (1 / (2 ** expoente)))
        else:
            soma = abs(soma + ((-1*1) / (2 ** expoente))) 
    else:
        print(f"{soma:.14f}")
        break

    
    
