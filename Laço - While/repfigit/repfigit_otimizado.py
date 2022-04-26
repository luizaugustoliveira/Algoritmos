valor = input()
print(int(valor[0]))
print(int(valor[1]))

penultimo_termo = int(valor[0])
ultimo_termo = int(valor[1])
soma = ultimo_termo + penultimo_termo

while True:
    if soma < int(valor):
        print(soma)
    
    ultimo = ultimo_termo
    ultimo_termo = soma
    soma = soma + ultimo
    
    if soma == int(valor):
        print(soma)
        print("---")
        print(f"{valor} é um repfigit.")
        break
    
    if soma > int(valor):
        print("---")
        print(f"{valor} não é um repfigit.")
        break