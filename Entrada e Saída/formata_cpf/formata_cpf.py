# UFCG
# Prog1
# Luiz Augusto Oliveira de Farias
# Matrícula: 120110389
# Questão: Formata CPF

cpf1 = int(input())
cpf2 = int(input())
cpf3 = int(input())

cp1_ultimo = cpf1 % 10
cp1_penultimo = cpf1 % 100 // 10
cpf1_inicio = cpf1 // 100

cp2_ultimo = cpf2 % 10
cp2_penultimo = cpf2 % 100 // 10
cpf2_inicio = cpf2 // 100

cp3_ultimo = cpf3 % 10
cp3_penultimo = cpf3 % 100 // 10
cpf3_inicio = cpf3 // 100

print(f"{cpf1_inicio}-{cp1_penultimo}{cp1_ultimo}")
print(cp1_ultimo + cp1_penultimo)

print(f"{cpf2_inicio}-{cp2_penultimo}{cp2_ultimo}")
print(cp2_ultimo + cp2_penultimo)

print(f"{cpf3_inicio}-{cp3_penultimo}{cp3_ultimo}")
print(cp3_ultimo + cp3_penultimo)
