# UFCG
# Prog1
# Luiz Augusto Oliveira de Farias
# Matrícula: 120110389
# Questão: Lei Estadual de Incentivo Cultural

idade = int(input("Idade? "))

if idade < 12:
  print("criança (meia entrada)")

elif idade > 65:
  print("idoso (meia entrada)")
  
elif idade >= 12 and idade <= 65:
  estudante = input("Estudante? ")
  if estudante == "s":
    rede = input("Rede Pública? ")
    if rede == "s":
      print("estudante da rede pública (isento)")
  else:
      print("estudante (meia entrada)")
else:
  print("adulto (inteira)")
