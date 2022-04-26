# UFCG
# Prog1
# Luiz Augusto Oliveira de Farias
# Matrícula: 120110389
# Questão: Gratificação Natalina

codigo = int(input())

if codigo == 1:
    print(f"Deverá receber em dezembro R$ 25000.00.")

elif codigo == 2:
    print(f"Deverá receber em dezembro R$ 15000.00.")

elif codigo == 3:
    dias_faltas = int(input())
    gratificacao = (235 - dias_faltas) * 2
    salario = 8000 + gratificacao

    if dias_faltas == 0:
        gratificacao = 500
        salario = 8500

    print(f"Valor da gratificação R$ {gratificacao:.2f}.")
    print(f"Deverá receber em dezembro R$ {salario:.2f}.")

elif codigo == 4:
    dias_faltas = int(input())
    gratificacao = (235 - dias_faltas) * 1
    salario = 5000 + gratificacao

    if dias_faltas == 0:
        gratificacao = 300
        salario = 5300

    print(f"Valor da gratificação R$ {gratificacao:.2f}.")
    print(f"Deverá receber em dezembro R$ {salario:.2f}.")

elif codigo == 5:
    dias_faltas = int(input())
    gratificacao = (235 - dias_faltas) * 0.7
    salario = 2800 + gratificacao

    if dias_faltas == 0:
        gratificacao = 200
        salario = 3000
        
    print(f"Valor da gratificação R$ {gratificacao:.2f}.")
    print(f"Deverá receber em dezembro R$ {salario:.2f}.")
