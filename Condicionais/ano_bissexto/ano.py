# UFCG
# Prog1
# Luiz Augusto Oliveira de Farias
# Matrícula: 120110389
# Questão: Ano Bissexto

num = int(input())
if num % 4 == 0 or num % 400 == 0 and num % 100 !=0:
    print(f"{num} é bissexto")
else:
    print(f"{num} não é bissexto")
