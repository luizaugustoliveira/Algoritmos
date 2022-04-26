def calculadora(entrada, num1, num2):        
    if entrada == 1:
        resultado = num1 + num2
        print(resultado)
    elif entrada == 2:
        resultado = num1 - num2
        print(resultado)
    elif entrada == 3:
        resultado = num1 * num2
        print(resultado)
    elif entrada == 4:
        resultado = int(num1 / num2)
        print(resultado)
    
    
while True:
    e = input().split()

    if int(e[0]) == 5: break

    if int(e[0]) == 4 and int(e[2]) == 0:
        print("Erro: Divisão por 0")
        break
     
    calculadora(int(e[0]), int(e[1]), int(e[2]))    
