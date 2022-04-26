# UFCG
# Prog1
# Luiz Augusto Oliveira de Farias
# Matrícula: 120110389
# Questão: Compatibilidade Sanguínea

paciente_abo = input()
paciente_rh = input()
doador_abo = input()
doador_rh = input()

if paciente_abo == 'A' and paciente_rh == '+':
    if doador_abo == 'A' or doador_abo == 'O':
        print('compatível')
    else:
        print('incompatível')
elif paciente_abo == 'A' and paciente_rh == '-':
    if doador_abo == 'A' or doador_abo == 'O':
        if doador_rh == '-':
            print('compatível')
        else:
            print('incompatível')
    else:
        print('incompatível')

elif paciente_abo == 'B' and paciente_rh == '+':
    if doador_abo == 'B' or doador_abo == 'O':
        print('compatível')
    else:
        print('incompatível')
elif paciente_abo == 'B' and paciente_rh == '-':
    if doador_abo == 'B' or doador_abo == 'O':
        if doador_rh == '-':
            print('compatível')
        else:
            print('incompatível')
    else:
        print('incompatível')

elif paciente_abo == 'AB' and paciente_rh == '+':
    print('compatível')
elif paciente_abo == 'AB' and paciente_rh == '-':
    if doador_rh == '-':
        print('compatível')
    else:
        print('incompatível')

elif paciente_abo == 'O' and paciente_rh == '+':
    if doador_abo == 'O':
        print('compatível')
    else:
        print('incompatível')
elif paciente_abo == 'O' and paciente_rh == '-':
    if doador_abo == 'O':
        if doador_rh == '-':
            print('compatível')
        else:
            print('incompatível')
    else:
        print('incompatível')
