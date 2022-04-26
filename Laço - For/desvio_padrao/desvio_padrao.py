# UFCG
# Prog1
# Luiz Augusto Oliveira de Farias
# Matrícula: 120110389
# Questão: Desvio Padrão

sequencia1 = input()
sequencia2 = input()

lista1 = sequencia1.split(" ")
soma1 = 0
for i in range(len(lista1)):
    soma1 += float(lista1[i])

media1 = soma1 / len(lista1)
lista_diferenca1 = []
for i in range(len(lista1)):
    diferenca1 = float(lista1[i]) - media1
    lista_diferenca1.append(diferenca1)

lista_quadrados1 = []
for i in range(len(lista_diferenca1)):
    quadrados1 = lista_diferenca1[i] ** 2
    lista_quadrados1.append(quadrados1)

soma_1 = 0
for i in range(len(lista_quadrados1)):
    soma_1 += lista_quadrados1[i] 

desvio_padrao1 = (soma_1 / (len(lista1) - 1)) ** 0.5

lista2 = sequencia2.split(" ")
soma2 = 0
for i in range(len(lista2)):
    soma2 += float(lista2[i])

media2 = soma2 / len(lista2)
lista_diferenca2 = []
for i in range(len(lista2)):
    diferenca2 = float(lista2[i]) - media2
    lista_diferenca2.append(diferenca2)

lista_quadrados2 = []
for i in range(len(lista_diferenca2)):
    quadrados2 = lista_diferenca2[i] ** 2
    lista_quadrados2.append(quadrados2)

soma_2 = 0
for i in range(len(lista_quadrados2)):
    soma_2 += lista_quadrados2[i] 

desvio_padrao2 = (soma_2 / (len(lista2) - 1)) ** 0.5

if desvio_padrao1 == desvio_padrao2:
    print(f"As sequências possuem o mesmo desvio padrão ({desvio_padrao1:.2f}).")
elif desvio_padrao1 > desvio_padrao2:
    print(f"A sequência 1 possui o maior desvio padrão ({desvio_padrao1:.2f}).")
else:
    print(f"A sequência 2 possui o maior desvio padrão ({desvio_padrao2:.2f}).")

    
    
     

