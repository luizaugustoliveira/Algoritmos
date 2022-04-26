# UFCG
# Prog1
# Luiz Augusto Oliveira de Farias
# Matrícula: 120110389
# Questão: Campeonato Brasileiro de Futebol 2020

pontos_a = int(input())
vitorias_a = int(input())
gols_marcados_a = int(input())
gols_sofridos_a = int(input())
pontos_b = int(input())
vitorias_b = int(input())
gols_marcados_b = int(input())
gols_sofridos_b = int(input())

saldo_a = gols_marcados_a - gols_sofridos_a
saldo_b = gols_marcados_b - gols_sofridos_b

if pontos_a > pontos_b:
  print("O Time A ganhou do Time B.")
elif pontos_b > pontos_a:
  print("O Time B ganhou do Time A.")

if pontos_a == pontos_b:
  if vitorias_a > vitorias_b:
    print("O Time A ganhou do Time B.")
  elif vitorias_b > vitorias_a:
    print("O Time B ganhou do Time A.")
  elif vitorias_a == vitorias_b:
    if saldo_a > saldo_b:
      print("O Time A ganhou do Time B.")
    elif saldo_b > saldo_a:
      print("O Time B ganhou do Time A.")
    else:
      print("Os dois times terminaram empatados.")
