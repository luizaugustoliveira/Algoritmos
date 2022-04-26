#luiz.augusto.farias@ccc.ufcg.edu.br

def calcula_venda(valor_compra, imposto1, imposto2, lucro_percent):       
    ipi = (imposto1 * valor_compra)
    iof = (imposto2 * valor_compra)
    impostos = ipi + iof
    lucro = lucro_percent * valor_compra
    valor_venda = valor_compra + impostos + lucro
    print(f"O valor de venda para este produto deve ser R$ {valor_venda:.2f}")
    return valor_venda

while True:
    entrada = input().split(", ")
    if entrada == ["-"]: break
    calcula_venda(float(entrada[0]), float(entrada[1]), float(entrada[2]), float(entrada[3]))
