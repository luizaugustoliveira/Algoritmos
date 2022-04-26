cliente = input().split()

conta = float(cliente[1])
#print(conta)

while True:
    op = input().split()
    if op[0] == '1':
        conta -= float(op[1])
    elif op[0] == '2':
        conta += float(op[1])
    elif op[0] == '3':
        break

print(f"Saldo de R$ {conta:.2f} na conta de {cliente[0]}")
    
    
