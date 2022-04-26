# UFCG
# Prog1
# Luiz Augusto Oliveira de Farias
# Matrícula: 120110389
# Questão: Tweets por página

t = int(input())

paginas = t // 400

paginas_completas = 400 * paginas

percent_perdidos = ((t - paginas_completas) / t) * 100

print(f"Serão necessárias {paginas} página(s) para visualizar os tweets.")
print(f"{percent_perdidos:.1f}% dos tweets serão perdidos.")
