# UFCG
# Prog1
# Luiz Augusto Oliveira de Farias
# Matrícula: 120110389
# Questão: DNA

seq1 = input()
seq2 = input()
seq3 = input()

a = len(seq1)
b = len(seq2)
c = len(seq3)

if a < b and a < c:
    print(f"{seq1} {a}")
elif b < a and b < c:
    print(f"{seq2} {b}")
elif c < a and c < b:
    print(f"{seq3} {c}")
elif a == b or a == c:
    print(f"{seq1} {a}")
elif b == c:
    print(f"{seq2} {b}")

