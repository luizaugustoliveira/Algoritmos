codigo = int(input())
if codigo == 3:
    dias_faltas = int(input())

if codigo == 1:
    print(f"Deverá receber em dezembro R$ 25000.00.")
elif codigo == 2:
    print(f"Deverá receber em dezembro R$ 15000.00.")
elif codigo == 3:
    dia_g = 2
    salario = 8000
    gratificacao = (235 - dias_faltas) * dia_g
    salario = 8000 + gratificacao
    if dias_faltas == 0:
        gratificacao = 500
        salario = 8500
    print(f"Valor da gratificação R$ {gratificacao:.2f}.")
    print(f"Deverá receber em dezembro R$ {salario:.2f}.")

