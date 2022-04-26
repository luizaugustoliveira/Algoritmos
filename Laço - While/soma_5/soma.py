# UFCG
# Prog1
# Luiz Augusto Oliveira de Farias
# luiz.augusto.farias@ccc.ufcg.edu.br
# Matrícula: 120110389
# Período: 2020.2e
# Data: 9 de setembro de 2021
# Questão: Soma 5 abaixo de 20

contador = 0
linha = 0
soma = 0
comparador = 20

while True:
  try:
    linha +=1
    
    valor_lido = int(input())
    if valor_lido < comparador: 
        contador += 1
        soma += valor_lido
    
    if contador == 5: break
    
    
  except EOFError:
    break
    
print(f"soma = {soma}")
print(f"5 menores que 20 até a linha {linha}")
