km = float(input())
tempo = float(input())

velocidade = km / tempo 

if velocidade < 10:
    print(f"Velocidade: {velocidade:.1f}km/h. Corredor amador.")
elif 10 < velocidade < 15:
    print(f"Velocidade: {velocidade:.1f}km/h. Corredor aspirante.")
elif velocidade > 15:
    print(f"Velocidade: {velocidade:.1f}km/h. Corredor profissional.")