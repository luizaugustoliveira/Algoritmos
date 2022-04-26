#Iterar todas as letras da chave no intuito de comparar depois com frase
#colocar um contador dentro do for porque ele precisa ser zerado muitas vezes 
#Se na frase tiver alguma letra igual a da chave
#Colocar na saída qual é essa letra e quantas vezes ela se repete

frase = input()
chave = input()

for i in chave:
    contador = 0
    for j in frase:
        if i == j:
            contador += 1
    print(f"{i} {contador}")
