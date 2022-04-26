# UFCG
# Prog1
# Luiz Augusto Oliveira de Farias
# Matrícula: 120110389
# Questão: Criação de uma Nova Palavra

palavra = input()
num = input()

lista = []
for i in range(len(num)-1 , -1 , -1):
    lista.append(i + 2)
#    print(i)
#print(lista)

nova_palavra = ""
for i in range(len(palavra)):
    nova_palavra += palavra[i] * lista[i]
print(nova_palavra)
    