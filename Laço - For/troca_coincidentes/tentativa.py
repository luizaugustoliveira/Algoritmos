palavra=input()
codigo=input()
npalavra=[]
ncodigo=[]
newpalavra=""
lista1=['0','1','2','3','4','5','6','7','8','9']
for i in range(len(palavra)):
    npalavra.append(palavra[i])
for k in range(len(codigo)):
    ncodigo.append(codigo[k])
for j in range(len(ncodigo)):
    if npalavra[j]!=lista1[j]:
        newpalavra+=npalavra[j]
    elif npalavra[j]==lista1[j]:
        newpalavra+=ncodigo[j]
for x in range(len(ncodigo),len(npalavra)):
    newpalavra+=npalavra[x]
print(newpalavra)
