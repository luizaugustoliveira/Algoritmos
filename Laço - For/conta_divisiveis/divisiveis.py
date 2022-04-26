# UFCG
# Prog1
# Luiz Augusto Oliveira de Farias
# Matrícula: 120110389
# Questão: Quantidade de Inteiros Divisíveis por K

num_k = int(input())
tam_seq_n = int(input())

quantidade = 0
lista = []
for valores in range(tam_seq_n):
  sequencia = int(input())
  if sequencia % num_k == 0:
    quantidade = quantidade + 1
    lista.append(sequencia)

percent = (quantidade * 100) / tam_seq_n
print(f"{quantidade} ({percent:.1f}%)")

