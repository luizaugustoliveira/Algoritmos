#UFCG
#Prog1
#Luiz Augusto Oliveira de Farias
#Matrícula: 120110389
#Questão: Salario

salario_bruto = float(input())
horas_de_trabalho = int(input())

ganhos_por_hora = salario_bruto / horas_de_trabalho

ir = 0.11 * salario_bruto
inss = 0.08 * salario_bruto
sindicato = 0.05 * salario_bruto
salario_liquido = salario_bruto - ir - inss - sindicato
hora_liquida = salario_liquido / horas_de_trabalho

print(f"Salário Bruto = {salario_bruto:.2f}")
print(f"Hora Bruta = {ganhos_por_hora:.2f}")
print(f"Desconto IR = {ir:.2f}")
print(f"Desconto INSS = {inss:.2f}")
print(f"Desconto Sindicato = {sindicato:.2f}")
print(f"Salário Líquido = {salario_liquido:.2f}")
print(f"Hora Líquida = {hora_liquida:.2f}")

