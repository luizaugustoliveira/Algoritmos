# UFCG
# Prog1
# Luiz Augusto Oliveira de Farias
# Matrícula: 120110389
# Questão: Criação de uma Nova Palavra

palavra = input()
num = input()

nova_palavra = ""
for i in range(len(palavra)):
#    nova_palavra += palavra[i]
    acumulador = str(palavra[i]) * int(num[-i - 1])
    nova_palavra += acumulador
print(nova_palavra)
