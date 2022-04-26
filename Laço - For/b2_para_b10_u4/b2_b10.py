# UFCG
# Prog1
# Luiz Augusto Oliveira de Farias
# Matrícula: 120110389
# Questão: Conversão de Número na Base 2 para a Base 10

binario = input()

lista_expoentes = []
for i in range(len(binario) -1, -1, -1):
    lista_expoentes.append(i)
print(lista_expoentes)

acumulador = 0
for k in range(len(binario)):
    i_binario = binario[k]
    expoente = 2 ** int(lista_expoentes[k])
    resultado = int(i_binario) * expoente
    acumulador += resultado
    print(f"{i_binario} * {expoente} = {resultado}")

print(f"{binario}(2) = {acumulador}(10)")




#    binario[i] * (2 ** (len(binario) - binario[-1]))