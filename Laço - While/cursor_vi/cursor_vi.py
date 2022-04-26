entrada = input()
v = entrada.split()

soma1 = int(v[0])
soma2 = int(v[1])
while True:
    cursor = input()
    if cursor == "": break

    valores = cursor.split()
    if valores[1] == "j":
        soma1 += int(valores[0])
        print(f"[{soma1} {soma2}]")

    if valores[1] == "l":
        soma2 += int(valores[0])
        print(f"[{soma1} {soma2}]")

    if valores[1] == "h":
        soma2 -= int(valores[0])
        print(f"[{soma1} {soma2}]")

    if valores[1] == "k":
        soma1 -= int(valores[0])
        print(f"[{soma1} {soma2}]")
        

