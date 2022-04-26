x = 0
y = 0
while True:
    entrada = input()
    valores = entrada.split()
    if valores[1] == "0":
        print("Fim de jogo")
        break

    if valores[0] == "D":
        x += int(valores[1])

    if valores[0] == "E":
        x -= int(valores[1])
    
    if valores[0] == "C":
        y += int(valores[1])

    if valores[0] == "B":
        y -= int(valores[1])

    if abs(y) == abs(2 * x):
        if x != 0 and y != 0:
            print(f"Parabéns, conquista do portal ({x}, {y})")
            break
