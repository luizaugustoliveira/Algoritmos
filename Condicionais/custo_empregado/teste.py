salario_bruto = float(input())
dias = int(input())
transporte = float(input())

valor_mensal_transporte = transporte * dias
custo_transporte = 0.06 * salario_bruto
custo_fgts_empregador = 0.08 * salario_bruto
custo_inss_empregador = 0.12 * salario_bruto

if valor_mensal_transporte > custo_transporte:
  custo_empresa_transporte = valor_mensal_transporte - custo_transporte

else:
  custo_transporte = 0.06*salario_bruto
  custo_empresa_transporte = 0


custos_empregador = salario_bruto + custo_empresa_transporte + custo_fgts_empregador + custo_inss_empregador

if salario_bruto <= 1317.07:
  inss_empregado = 0.08 * salario_bruto
elif salario_bruto >= 1317.08 and salario_bruto <= 2195.12:
  inss_empregado = 0.09 * salario_bruto
else:
  inss_empregado = 0.11 * salario_bruto

descontos_empregado = custo_transporte + inss_empregado

salario_liquido = salario_bruto - descontos_empregado

print(f"salário bruto = R$ {salario_bruto:.2f}")
print(f"custo mensal = R$ {custos_empregador:.2f}")
print(f"salário líquido = R$ {salario_liquido:.2f}")

