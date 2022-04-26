valor_forca = int(input())

if 0 < valor_forca < 90:
  mensagem = "Quadrante 1"
elif 90 < valor_forca < 180:
  mensagem = "Quadrante 2"
elif 180 < valor_forca < 270:
  mensagem = "Quadrante 3"
elif 270 < valor_forca < 360:
  mensagem = "Quadrante 4"

if valor_forca == 0 or valor_forca == 90 or valor_forca == 180 or valor_forca == 270 or valor_forca == 360:
  mensagem = "Sobre eixos"

if valor_forca > 360:
  calculo = valor_forca % 360
  if 0 < calculo < 90:
    mensagem = "Quadrante 1"
  elif 90 < calculo < 180:
    mensagem = "Quadrante 2"
  elif 180 < calculo < 270:
    mensagem = "Quadrante 3"
  elif 270 < calculo < 360:
    mensagem = "Quadrante 4"
  else:
      mensagem = "Sobre eixos"  
    
print(mensagem)