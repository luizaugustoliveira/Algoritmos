# UFCG
# Prog1
# Luiz Augusto Oliveira de Farias
# Matrícula: 120110389
# Questão: Status unidade

quantidade_mt = int(input())

if quantidade_mt == 1:
    nota1 = float(input())
    media = nota1 / quantidade_mt
    print(media)
    if media >= 6:
        print("Aluno aprovado na unidade")
    else:
        print("Aluno ainda não aprovado na unidade")
elif quantidade_mt == 2:
    nota1 = float(input())
    nota2 = float(input())
    media = (nota1 + nota2) / quantidade_mt
    print(media)
    if media >= 6:
        print("Aluno aprovado na unidade")
    else:
        print("Aluno ainda não aprovado na unidade")
elif quantidade_mt == 3:
    nota1 = float(input())
    nota2 = float(input())
    nota3 = float(input())
    media = ((nota1 + nota2 + nota3) / quantidade_mt) - 0.5
    print(media)
    if media >= 6:
        print("Aluno aprovado na unidade")
    else:
        print("Aluno ainda não aprovado na unidade")
elif quantidade_mt == 4:
    nota1 = float(input())
    nota2 = float(input())
    nota3 = float(input())
    nota4 = float(input())
    media = ((nota1 + nota2 + nota3 + nota4) / quantidade_mt) - 0.5
    print(media)
    if media >= 6:
        print("Aluno aprovado na unidade")
    else:
        print("Aluno ainda não aprovado na unidade")


