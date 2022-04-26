# UFCG
# Prog1
# Luiz Augusto Oliveira de Farias
# Matrícula: 120110389
# Questão: Custo Empregado

salario_bruto = float(input())
dias_trabalho = int(input())
custo_diario_transporte = float(input())

custo_mensal_transporte = custo_diario_transporte * dias_trabalho

porcentagem_custo_transporte = (custo_mensal_transporte / salario_bruto) * 100

if porcentagem_custo_transporte < 6:
    vale_transporte_empresa = 0
    vale_transporte_empregado = custo_mensal_transporte
else:
    vale_transporte_empregado = 0.06 * salario_bruto
    vale_transporte_empresa = custo_mensal_transporte - vale_transporte_empregado

fgts_empregador = 0.08 * salario_bruto
inss_empregador = 0.12 * salario_bruto

custo_mensal = fgts_empregador + inss_empregador + vale_transporte_empresa + salario_bruto

if salario_bruto <= 1317.07:
  inss_empregado = salario_bruto * 0.08
elif salario_bruto > 2195.13:
  inss_empregado = salario_bruto * 0.11
else:
  inss_empregado = salario_bruto * 0.09

salario_liquido = salario_bruto - inss_empregado - vale_transporte_empregado

print(f"salário bruto = R$ {salario_bruto:.2f}")
print(f"custo mensal = R$ {custo_mensal:.2f}")
print(f"salário líquido = R$ {salario_liquido:.2f}")
