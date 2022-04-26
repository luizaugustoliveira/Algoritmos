m = int(input())
caixas = m //400
perda = ((m - (caixas*400))/m) * 100
print(f'{caixas} caixa(s) completa(s) para embalar os morangos.')
print(f'{perda:.1f}% dos morangos serão perdidos.')