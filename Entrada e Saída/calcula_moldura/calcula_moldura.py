# UFCG
# Prog1
# Luiz Augusto Oliveira de Farias
# Matrícula: 120110389
# Questão: Calcula Moldura

comprimento = float(input())
largura = float(input())

p_comprimento = ((comprimento * 2) / 100) * 120
p_largura = ((largura * 2) / 100) * 120
preco = p_comprimento + p_largura

print(f"R$ {preco:.1f}")
