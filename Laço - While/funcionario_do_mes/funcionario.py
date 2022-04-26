#luiz.augusto.farias@ccc.ufcg.edu.br

def maior(lista):
    posicao_do_maior = 0
    for i in range(len(lista)):
        if lista[i] > lista[posicao_do_maior]:
            posicao_do_maior = i
    return posicao_do_maior

funcionarios = []
producoes = []

while True:
    nome = input()
    if nome == "fim": break

    soma = 0
    while True:
        producao = input()
        if producao == "-": break
        soma += int(producao)
    
    funcionarios.append(nome)
    producoes.append(soma)

print(funcionarios[maior(producoes)])
print(producoes[maior(producoes)])



