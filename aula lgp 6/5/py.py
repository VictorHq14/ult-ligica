media = 0
for i in range(4):
  nota = float(input("digit sua nota:  "))
  media += nota
  mediageral = media / 4
if mediageral >= 6:
  print("aprovado")
else:
  print("reprovado")
