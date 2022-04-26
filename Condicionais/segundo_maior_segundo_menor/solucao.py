n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())

maior = 0
segundo_maior = 0
terceiro_maior = 0
quarto_maior = 0

if n1 > n2:
    maior = n1
    segundo_maior = n2
else:
    maior = n2
    segundo_maior = n1

if n3 > maior:
    terceiro_maior = segundo_maior
    segundo_maior = maior
    maior = n3
elif n3 > segundo_maior:
    terceiro_maior = segundo_maior
    segundo_maior = n3
else:
    terceiro_maior = n3

if n4 > maior:
    quarto_maior = terceiro_maior
    terceiro_maior = segundo_maior
    segundo_maior = maior
    maior = n4
elif n4 > segundo_maior:
    quarto_maior = terceiro_maior
    terceiro_maior = segundo_maior
    segundo_maior = n4
elif n4 > terceiro_maior:
    quarto_maior = terceiro_maior
    terceiro_maior = n4
else:
    quarto_maior = n4

print(f"Considerando os números {n1}, {n2}, {n3} e {n4}")
print(f"""O segundo menor número é {terceiro_maior}
O segundo maior número é {segundo_maior}""")