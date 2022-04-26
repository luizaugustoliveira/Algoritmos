# UFCG
# Prog1
# Luiz Augusto Oliveira de Farias
# Matrícula: 120110389
# Questão: Cadastro Nacional de Pessoa Jurídica - CNPJ

cnpj = input()

soma = int(cnpj[0]) + int(cnpj[1]) + int(cnpj[3]) + int(cnpj[4]) + int(cnpj[5]) + int(cnpj[7]) + int(cnpj[8]) + int(cnpj[9]) + 1

print(f"{cnpj}/0001-{soma:02d}")
