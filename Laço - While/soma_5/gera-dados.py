import sys
import random

N = 1000000 if len(sys.argv) < 2 else int(sys.argv[1])

seed = '' if len(sys.argv) < 3 else sys.argv[2]
random.seed(seed)

with open("dados.txt", mode="w") as arq:
    for i in range(N):
        valor = random.randint(0, 1000000)
        arq.write(f"{valor}\n")
