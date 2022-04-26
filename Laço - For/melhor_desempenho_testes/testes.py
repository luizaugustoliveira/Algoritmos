# UFCG
# Prog1
# Luiz Augusto Oliveira de Farias
# Matrícula: 120110389
# Questão: Melhor Desempenho por Teste

alunos = int(input())

lista_linhas = [] 

for linha in range(alunos):
    linha = input()
    lista_linhas.append(linha)

lista_linhas = ['...**FFf', '.fffff**', '.****.ff'] 

#soma = 0
#for c in lista_linhas:
#  if "." in c:
#    soma = soma + 1
#print(soma)

melhor_aluno = lista_linhas[0]
soma = 0
for c in lista_linhas[0]:
      if c == ".":
              soma = soma + 1
              print(soma)
               
               for indice in range(len(lista_linhas)):
                     if indice > lista_linhas[0]:
                             melhor_aluno = indice

                             print(indice)


#melhor_aluno = -1
#for c in 



#soma = 0
#for c in lista_linhas:
#    if c == ".":
#        soma = soma + 1



#soma = 0
#for posicao in range(len(lista_linhas)):
#    if "." in sequencia[posicao]:
#        soma = soma + 1


soma = 0
for c in lista_linhas:
    if c == ".":
        soma = soma + 1

print(lista_linhas)
print(soma)

