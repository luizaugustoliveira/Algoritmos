# luiz.augusto.farias@ccc.ufcg.edu.br
# 120110389

soma = 0
palavras = []
while True:
    entrada = input()
    if entrada == "fim": break
    palavras.append(entrada)
    valor = len(entrada)
    soma += valor

media = soma / len(palavras)
print(f"{media:.2f}")

for i in range(len(palavras)):
    if len(palavras[i]) > media:
        print(f"{i + 1} {palavras[i]}")
