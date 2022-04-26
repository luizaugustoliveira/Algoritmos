# UFCG
# Prog1
# Luiz Augusto Oliveira de Farias
# Matrícula: 120110389
# Questão: Lucro Mensal de uma Empresa

lista_entrada = []
for entrada in range(12):
  entrada = input()
  lista_entrada.append(entrada)

lista = []
mes = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
for i in range(len(lista_entrada)):
    receita, despesa  = lista_entrada[i].split()
    
    l = float(receita) - float(despesa)
    
    lista.append(f"{mes[i]} {l:4.1f}")

for e in lista:
    print(e)
