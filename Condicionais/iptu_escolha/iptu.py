# UFCG
# Prog1
# Luiz Augusto Oliveira de Farias
# Matrícula: 120110389
# Questão: IPTU Escolhendo Forma de Pagamento

area = float(input())
metro_quadrado = float(input())
pagamento = input()

imposto = area * metro_quadrado 

if pagamento == "vista":
    valor = imposto * 0.8
    print(f"Total: R$ {valor:.2f}")

elif pagamento == "2x":
    valor = imposto * 0.9
    parcelas = valor / 2
    print(f"Total: R$ {valor:.2f}. Parcelas: R$ {parcelas:.2f}")

else:
    valor = imposto * 0.95
    parcelas = valor / 3
    print(f"Total: R$ {valor:.2f}. Parcelas: R$ {parcelas:.2f}")
