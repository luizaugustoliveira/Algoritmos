def repetido(sequencia):
    for i in range(len(sequencia) - 1):
        if sequencia[i] == sequencia[i+1]:
            return True
    return False

num = int(input())

com = 0
sem = 0
lista_com = []
lista_sem = []
for i in range(num):
    palavras = input()
    if repetido(palavras) == True:
        com += 1
        lista_com.append(palavras)
    elif repetido(palavras) == False:
        sem += 1
        lista_sem.append(palavras)

#print(com, sem, lista_com, lista_sem)

print(f"{com} palavra(s) com letras dobradas:")
for elemento in lista_com:
    print(elemento)

print("---")

print(f"{sem} palavra(s) sem letras dobradas:")
for elemento in lista_sem:
    print(elemento)






            
        

