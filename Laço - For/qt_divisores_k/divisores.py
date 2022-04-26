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
  inteiros = int(input())
  if inteiros % num_k == 0:
    quantidade = quantidade + 1
    lista.append(inteiros)

percent = (quantidade * 100) / tam_seq_n
print(f"{quantidade} ({percent:.1f}%)")


#percent = (quantidade / tam_seq_n) * 100
#tam_seq_n = 100
#quantidade = x

#num_k = int(input())
#tam_seq_n = int(input())

#lista = []
#for valores in range(tam_seq_n):
#  sequencia = int(input())
#  lista.append(sequencia)
#  quantidade = 0
#  for elemento in lista:
#    if elemento % num_k == 0:
#      quantidade = quantidade + 1
#      percent = (quantidade / tam_seq_n) * 100

#print(f"{quantidade} ({percent:.1f}%)")
