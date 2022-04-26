#luiz.augusto.farias@ccc.ufcg.edu.br

num = int(input())

lista = []
numero = abs(num)
while True:
    valor = numero % 10
    lista.append(valor) 
    numero = numero // 10
    if numero == 0: break

for i in range(len(lista)):
    print(lista[i])
    

    
    


