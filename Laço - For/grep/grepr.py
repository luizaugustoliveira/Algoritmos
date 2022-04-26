palavra = input()
num = int(input())

# a = palavra
# b == frase

for k in range(num):
    caracteres = 0
    frase = input()
    for i in range(len(frase)):
        if palavra[caracteres] == frase[i]:
            caracteres += 1
        else:
            caracteres = 0
        if caracteres == len(palavra):
            print(frase) 