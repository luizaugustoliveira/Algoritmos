# UFCG
# Prog1
# Luiz Augusto Oliveira de Farias
# Matrícula: 120110389
# Questão: Fundo de Investimento

lista_entrada = []
soma = 0
while True:
    entrada = float(input())
    lista_entrada.append(entrada)
    soma += entrada
    media = soma / len(lista_entrada)
    if entrada < media:
        lista_entrada.pop()
        soma -= entrada
        media = soma / len(lista_entrada)
        break

print(f"""Saldo total do FIS: R${soma:.2f}.
Média das contribuições: R${media:.2f}.""")