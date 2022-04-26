maior = 0
segundo_maior = 0
segundo_menor = 0

num1 = int(input())
num2 = int(input())

if num1 > num2:
    maior = num1
    segundo_maior = num2
elif num2 > num1:
    maior = num2
    segundo_maior = num1

num3 = int(input())

if maior == num1:
    if num3 > num1:
        maior = num3
        segundo_maior = num1
        segundo_menor = num2
    elif num3 < num1:
        if num3 > num2:
            maior = num1
            segundo_maior = num3
            segundo_menor = num2
        elif num3 < num2:
            maior = num1
            segundo_maior = num2
            segundo_menor = num3
        
if maior == num2:
    if num3 > num2:
        maior = num3
        segundo_maior = num2
        segundo_menor = num1
    elif num3 < num2:
        if num3 > num1:
            maior = num2
            segundo_maior = num3
            segundo_menor = num1
        elif num3 < num1:
            maior = num2
            segundo_maior = num1
            segundo_menor = num3

num4 = int(input())

if segundo_maior < num4 < maior:
    segundo_maior = num4
elif segundo_menor < num4 < segundo_maior :
    segundo_menor = num4

print(f"Considerando os números {num1}, {num2}, {num3} e {num4}")
print(f"""O segundo menor número é {segundo_menor}
O segundo maior número é {segundo_maior})
