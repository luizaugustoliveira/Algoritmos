#UFCG
#Prog1
#Luiz Augusto Oliveira de Farias
#Matrícula: 120110389
#Questão: Resumo das Vendas

num_loja = int(input())
num_teresa = int(input())
num_carla = int(input())

porcent_teresa = (num_teresa/num_loja) * 100
porcent_carla = (num_carla/num_loja) * 100
num_joaquim = num_loja - num_teresa - num_carla
porcent_joaquim = (num_joaquim /num_loja) * 100

print(f"Teresa vendeu {num_teresa} (de {num_loja}) brinquedos. ({porcent_teresa:.2f}%)")
print(f"Joaquim vendeu {num_joaquim} (de {num_loja}) brinquedos. ({porcent_joaquim:.2f}%)")
print(f"Carla vendeu {num_carla} (de {num_loja}) brinquedos. ({porcent_carla:.2f}%)")
