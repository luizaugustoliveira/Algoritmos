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
for lucro in lista_entrada:
    receita, despesa  = lucro.split()
    lista.append(float(receita))
    lista.append(float(despesa))
    l = float(receita) - float(despesa)
    print(f"{l:4.1f}")

lista_entrada = []
for entrada in range(12):
  entrada = input()
  lista_entrada.append(entrada)
  
lista = []
mes = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
for lucro in lista_entrada:
    receita, despesa  = lucro.split()
    lista.append(float(receita))
    lista.append(float(despesa))
    l = float(receita) - float(despesa)
    print(f"{l:8.1f}")

for elemento in mes:
    print(elemento)

print(f"{l:4.1f}")

#print(lista_entrada)
#print(lista)
    

#  receita = float(entrada[0:2])
#  despesa = float(entrada[-3:])
#  print(lucro)
#  print(despesa)
#  lucro = receita - despesa
#  print(lucro)

#tentativa

