dividendo = int(input())
divisor = int(input())
quociente = 0
resto = 0

dividendo_original = dividendo

while dividendo >= divisor:
    dividendo -= divisor
    quociente += 1
    resto = dividendo_original - quociente*divisor

print(f"quociente = {quociente} e resto = {resto}")