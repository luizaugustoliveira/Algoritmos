def vogais_primeiro(frase):
  acumulador = ""
  vogais = "AaEeIiOoUu"
  consoantes = ""
  for elemento in frase:
    if elemento in vogais:
      acumulador += elemento
    else:
      consoantes += elemento

  return acumulador + consoantes


print(vogais_primeiro("exemplo"))