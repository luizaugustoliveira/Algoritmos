def calculadora():
    while True:
        e = input().split()
        entrada = int(e[0])
        num1 = int(e[1])
        num2 = int(e[2])
        
        if entrada == 5: break

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
            if num2 == 0:
                print("Erro: Divisão por 0")
                break
            else:
                resultado = int(num1 / num2)
                print(resultado)
    
calculadora()
