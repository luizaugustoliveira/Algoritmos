# UFCG
# Prog1
# Luiz Augusto Oliveira de Farias
# Matrícula: 120110389
# Questão: Orçamento Nome

nome = input("Nome? ")
valor = float(input("Valor da letra (R$)? "))

num_letras = len(nome)
orcamento = num_letras * valor

print(f"Preço final: R$ {orcamento:.2f}")

