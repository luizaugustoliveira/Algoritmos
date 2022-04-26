#UFCG
#Prog1
#Luiz Augusto Oliveira de Farias
#Matrícula: 120110389
#Questão: Peso e IMC

peso = float(input())
altura = float(input())

imc = peso / altura ** 2

novo_peso = 24.9 * altura ** 2   

diferenca_peso = novo_peso - peso

print(f"IMC atual = {imc:.2f}")
print(f"Peso a ser ganho/perdido = {diferenca_peso:.2f}")
