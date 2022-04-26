# UFCG
# Prog1
# Luiz Augusto Oliveira de Farias
# Matrícula: 120110389
# Questão: Melhor Desempenho por Teste

num_alunos = int(input())

melhor_aluno = -1
maior_qt_acertos = 0

for linha in range(1, num_alunos + 1):
    resultado = input()

    quantidade_acertos = 0
    for caractere in resultado:
        if caractere == ".":
            quantidade_acertos = quantidade_acertos + 1

    if quantidade_acertos > maior_qt_acertos:
        maior_qt_acertos = quantidade_acertos
        melhor_aluno = linha

print(melhor_aluno)

