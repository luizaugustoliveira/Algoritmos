#UFCG
#Prog1
#Luiz Augusto Oliveira de Farias
#Matrícula: 120110389
#Questão: Orçamento Construção

preco_unidade_tijolo = float(input("Digite o preço da unidade do tijolo (Em reais): "))
altura_tijolo = float(input("Digite a altura do tijolo (Em metros): "))
comprimento_tijolo = float(input("Digite o comprimento do tijolo (Em metros): "))
altura_parede = float(input("Digite a altura das paredes (Em metros): "))
comprimento_parede = float(input("Digite o comprimento das paredes (Em metros): "))

numero_tijolos = (altura_parede/altura_tijolo) * (comprimento_parede/comprimento_tijolo)  
orcamento = preco_unidade_tijolo * numero_tijolos

print(f"O número total de tijolos é {numero_tijolos:.1f} e o orçamento final é de R$ {orcamento:.1f}")

