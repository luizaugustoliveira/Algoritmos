# UFCG
# Prog1
# Luiz Augusto Oliveira de Farias
# Matrícula: 120110389
# Questão: Compatibilidade Sanguínea

abo_receptor = input()
rh_receptor = input()
abo_doador = input()
rh_doador = input()

if abo_receptor == "A" and rh_receptor == "+":
  if abo_doador == "A" and rh_doador == "+" or abo_doador == "A" and rh_doador == "-" or abo_doador == "O" and rh_doador == "+" or abo_doador == "O" and rh_doador == "-": 
    print("compatível")
  else:
    print("incompatível")
elif abo_receptor == "A" and rh_receptor == "-":
  if abo_doador == "A" and rh_doador == "-" or abo_doador == "O" and rh_doador == "-":
    print("compatível")
  else:
    print("incompatível")
elif abo_receptor == "B" and rh_receptor == "+":
  if abo_doador == "B" and rh_doador == "+" or abo_doador == "B" and rh_doador == "-" or abo_doador == "O" and rh_doador == "+" or abo_doador == "O" and rh_doador == "-":
    print("compatível")
  else:
    print("incompatível")
elif abo_receptor == "B" and rh_receptor == "-":
  if abo_doador == "B" and rh_doador == "-" and abo_doador == "O" and rh_doador == "-":
    print("compatível")
  else:
    print("incompatível")
elif abo_receptor == "AB" and rh_receptor == "+":
  if abo_doador == "AB" and rh_doador == "+" or abo_doador == "AB" and rh_doador == "-" or abo_doador == "A" and rh_doador == "+" or abo_doador == "A" and rh_doador == "-" or abo_doador == "O" and rh_doador == "+" or abo_doador == "O" and rh_doador == "-" or abo_doador == "B" and rh_doador == "+" or abo_doador == "B" and rh_doador == "-":
    print("compatível")
elif abo_receptor == "AB" and rh_receptor == "-":
  if abo_doador == "A" and rh_doador == "-" or abo_doador == "B" and rh_doador == "-" or abo_doador == "AB" and rh_doador == "-" or abo_doador == "O" and rh_doador == "-":
    print("compatível")
  else:
    print("incompatível")
elif abo_receptor == "O" and rh_receptor == "+":
  if abo_doador == "O" and rh_doador == "+" or abo_doador == "O" and rh_doador == "-":
     print("compatível")
  else:
    print("incompatível")
elif abo_receptor == "O" and rh_receptor == "-":
  if abo_doador == "O" and rh_doador == "-":
    print("compatível")
  else:
    print("incompatível")
