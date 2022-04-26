#UFCG
#Prog1
#Luiz Augusto Oliveira de Farias
#Matrícula: 120110389
#Questão: Nota na Final

print("== Estágio 1 ==")
peso1 = float(input("Peso? "))
nota1 = float(input("Nota? "))
print("== Estágio 2 ==")
peso2 = float(input("Peso? "))
nota2 = float(input("Nota? "))
print("== Estágio 3 ==")
peso3 = float(input("Peso? "))
nota3 = float(input("Nota? "))
print("== Resultados ==")

parcial = (peso1 * nota1) + (peso2 * nota2) + (peso3 * nota3)

notaf5 = (5 - (0.6 * parcial)) / 0.4
notaf7 = (7 - (0.6 * parcial)) / 0.4

print(f"Média parcial: {parcial:.1f}")
print(f"Nota na final, pra média 5.0 = {notaf5:.1f}")
print(f"Nota na final, pra média 7.0 = {notaf7:.1f}")
