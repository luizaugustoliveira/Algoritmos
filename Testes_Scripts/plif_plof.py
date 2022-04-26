num1 = int(input())
num2 = int(input())
num3 = int(input())

soma = num1 + num2 + num3

if soma % 3 == 0:
    print("plif")
elif soma % 5 == 0:
    print("plof")
elif soma % 3 == 0 or soma % 5 == 0:
    print("plifplof")
else:
    print(soma)
