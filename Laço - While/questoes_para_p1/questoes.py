# UFCG
# Prog1
# Luiz Augusto Oliveira de Farias
# Matrícula: 120110389
# Questão: Questões para P1

nomes = []
valores = []
while True:
    entrada = input()
    if entrada == "**": break
    nomes.append(entrada)

    soma = 0
    while True:
        quantidades = input()
        if quantidades == "*": break
        soma += int(quantidades)
    valores.append(soma)
            
print(f"Relatório de novas questões:\n")

for i in range(len(nomes)):
    nome = nomes[i]
    valor = valores[i]
    print(f"{nome}: {valor}")

total = 0
for i in range(len(valores)):
    total += valores[i]
    
print(f"""---
Total de novas questões: {total}""")



