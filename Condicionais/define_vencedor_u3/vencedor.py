# luiz.augusto.farias@ccc.ufcg.edu.br 

nome1 = input()
n1 = int(input())
n2 = int(input())
n3 = int(input())

maior = 0
segundo_maior = 0
terceiro_maior = 0

if n1 > n2:
    maior = n1
    segundo_maior = n2
else:
    maior = n2
    segundo_maior = n1

if n3 > maior:
    terceiro_maior = segundo_maior
    segundo_maior = maior
    maior = n3
elif n3 > segundo_maior:
    terceiro_maior = segundo_maior
    segundo_maior = n3
else:
    terceiro_maior = n3

media_1 = (maior + terceiro_maior) / 2
 
nome2 = input()
n4 = int(input())
n5 = int(input())
n6 = int(input())

maior_ = 0
segundo_maior_ = 0
terceiro_maior_ = 0

if n4 > n5:
    maior_ = n4
    segundo_maior_ = n5
else:
    maior_ = n5
    segundo_maior_ = n4

if n6 > maior_:
    terceiro_maior_ = segundo_maior_
    segundo_maior_ = maior_
    maior_ = n6
elif n6 > segundo_maior_:
    terceiro_maior_ = segundo_maior_
    segundo_maior_ = n6
else:
    terceiro_maior_ = n6

media_2 = (maior_ + terceiro_maior_) / 2

if media_1 > media_2:
    print(f"{nome1} venceu com nota {media_1}.")
elif media_2 > media_1:
    print(f"{nome2} venceu com nota {media_2}.")

if media_1 == media_2:
    if maior > maior_:
        print(f"{nome1} venceu (no critério de desempate) com nota {media_1}.")
    elif maior_ > maior:
        print(f"{nome2} venceu (no critério de desempate) com nota {media_2}.")
    else:
        print(f"{nome1} e {nome2} venceram com nota 20.0.")
        
