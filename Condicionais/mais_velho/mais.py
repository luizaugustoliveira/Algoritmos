# UFCG
# Prog1
# Luiz Augusto Oliveira de Farias
# Matrícula: 120110389
# Questão: Mais velho entre duas pessoas

pessoa1 = input()
dia1 = int(input())
mes1 = int(input())
ano1 = int(input())
pessoa2 = input()
dia2 = int(input())
mes2 = int(input())
ano2 = int(input())

if ano1 < ano2:
  print(pessoa1)
elif ano2 < ano1: 
  print(pessoa2)
elif ano1 == ano2:
  if mes1 < mes2:
    print(pessoa1)
  elif mes2 < mes1:
    print(pessoa2)
elif ano1 == ano2 and mes1 == mes2:
  if dia1 < dia2:
    print(pessoa1)
  elif dia2 < dia1:
    print(pessoa2)
elif ano1 == ano2 and mes1 == mes2 and dia1 == dia2:
  print("nenhuma")
