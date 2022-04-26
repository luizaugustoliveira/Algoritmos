#UFCG
#Prog1
#Luiz Augusto Oliveira de Farias
#Matrícula: 120110389
#Questão: Média Ponderada

nota1 = float(input())
nota2 = float(input())
nota3 = float(input())

peso1 = float(input())
peso2 = float(input())

peso3 = 100 - peso1 - peso2

npeso1 = peso1/100
npeso2 = peso2/100
npeso3 = peso3/100

media = (nota1*npeso1) + (nota2*npeso2) + (nota3*npeso3)

print(f"Média Final: {media:.1f}")
