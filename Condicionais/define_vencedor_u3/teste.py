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