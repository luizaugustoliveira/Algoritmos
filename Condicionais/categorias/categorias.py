# UFCG
# Prog1
# Luiz Augusto Oliveira de Farias
# Matrícula: 120110389
# Questão: Categorias

nome = input()
idade = int(input())

if 5 <= idade <= 7:
    print(f"{nome}, {idade} anos, Infantil A.")
elif 8 <= idade <= 10:
    print(f"{nome}, {idade} anos, Infantil B.")
elif 11 <= idade <= 13:
    print(f"{nome}, {idade} anos, Juvenil A.")
elif 14 <= idade <= 17:
    print(f"{nome}, {idade} anos, Juvenil B.")
elif idade > 17:
    print(f"{nome}, {idade} anos, Senior.")
else:
    print(f"{nome}, {idade} anos, Não pode competir.")
    
