#UFCG
#Prog1
#Luiz Augusto Oliveira de Farias
#Matrícula: 120110389
#Questão: O primeiro e o último dígito de um inteiro

num = int(input())

primeiro = int(num / 1000)
ultimo = num % 10

print(f"{primeiro} {ultimo}")
