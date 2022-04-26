# luiz.augusto.farias@ccc.ufcg.edu.br   

def quantidade_usuarios(cadastro):
    soma = 0
    for keys,valores in cadastro.items():
        if keys != 9999:
            soma += len(valores)
    
    return soma 


lsd = {1234:['Andrey'], 1226:['Nazareno', 'Livia'], 9999:['administrador'] }
deq = {1114:['Ana'] }

assert quantidade_usuarios(lsd) == 3
assert quantidade_usuarios(deq) == 1