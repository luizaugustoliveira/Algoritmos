# UFCG
# Prog1
# Luiz Augusto Oliveira de Farias
# Matrícula: 120110389
# Questão: Encontra elemento

num = int(input())
sequencia = input().split()

existe = False
for i in range(len(sequencia)):
    contador = 0
    if int(sequencia[i]) == num:
        existe = True
        break
    
    palavra = ""
    if int(sequencia[i]) != num:
        existe = False
        
if existe == True:
    print("sim")
else:
    print("não")
    
        
        
    


