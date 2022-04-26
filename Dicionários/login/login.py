# luiz.augusto.farias@ccc.ufcg.edu.br
# dicionarios --

def login(dicionario, email, senha):
    validacao = False
    for senhaa in dicionario.keys():
        if senhaa == senha:
            emails = dicionario[senhaa]
            for i in range(len(emails)):
                if emails[i] == email:
                    validacao = True

    return validacao


dados = {1313:['j@gmail.com'], 1226:['e@cc.com', 'd@cc.com'], 1507:['pedro@cc.com'] }
assert login(dados, 'd@cc.com',1313) == False
assert login(dados, 'd@cc.com', 1226) == True
assert login(dados, 'joao@gmail.com', 123) == False