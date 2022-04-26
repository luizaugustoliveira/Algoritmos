# UFCG
# Prog1
# Luiz Augusto Oliveira de Farias
# Matrícula: 120110389
# Questão: Calculo do IMC

#teste

peso = float(input())
altura = float(input())

imc = peso / (altura ** 2)

if imc < 18.5:
    print(f"IMC = {imc:.1f}")
    print("Classificação = Magreza")
elif imc >= 30:
    print(f"IMC = {imc:.1f}")
    print("Classificação = Obesidade")
elif 18.5 <= imc < 25:
    print(f"IMC = {imc:.1f}")
    print("Classificação = Saudável")
elif 25  <= imc < 30:
    print(f"IMC = {imc:.1f}")
    print("Classificação = Sobrepeso")
