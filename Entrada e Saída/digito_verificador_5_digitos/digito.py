# UFCG
# Prog1
# Luiz Augusto Oliveira de Farias
# Matrícula: 120110389
# Questão: Dígito Verificador de 5 Dígitos

num = input()

algarismo1 = int(num[0])
algarismo2 = int(num[1])
algarismo3 = int(num[2])
algarismo4 = int(num[3])
algarismo5 = int(num[4])

soma_num = algarismo1 + algarismo2 + algarismo3 + algarismo4 + algarismo5

digito_verificador = soma_num % 11

print(f"{num}-{digito_verificador:02d}")
