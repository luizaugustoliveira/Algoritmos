#UFCG
#Prog1
#Luiz Augusto Oliveira de Farias
#Matrícula: 120110389
#Questão: Resumo da passagem

identificador = input()
horario = input()
assento = input()
portao = input()
preco_sem_imposto = float(input())
preco_total = float(input())

porcentagem_de_imposto = ((preco_total - preco_sem_imposto) * 100) / preco_total

print('### Cartão de Embarque ###')
print(f'Identificador do voo: {identificador}')
print(f'Horário: {horario}')
print(f'Assento: {assento}')
print(f'Portão: {portao}')
print(f'Total de Imposto: {porcentagem_de_imposto:.1f}%')
