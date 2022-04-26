numero = input()
valor_limite = int(input())

i = 0
impares = 0
soma = 0
tamanho_string = len(numero)
criterio = ""
while True:
    if impares == 6:
        criterio += "6 ímpares"
        break

    if soma >= valor_limite: 
        criterio += "limite"
        break
    
    if i > tamanho_string - 1:
        criterio += "final da sequência"
        break

    if int(numero[i]) % 2 == 1:
        impares += 1
    
    soma += int(numero[i])
    i += 1

print(f"soma: {soma}")
print(f"números lidos: {impares} de {tamanho_string}")
print(f"critério de parada: {criterio}")
