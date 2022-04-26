my_list = ['p', 'q']
n = 4

nova_lista = []
for i in range(1, n + 1):
    for j in my_list:
        nova_lista.append(f"{j}{i}")

print(nova_lista)
