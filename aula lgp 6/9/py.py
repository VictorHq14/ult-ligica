
idade = float(input("digite sua idade: "))
if idade > 0:
  if idade >= 60:
    print("você é idoso")
  elif idade < 14:
    print("você é criança")
  elif idade >= 18:
    print("você é adulto")
  else:
    print("você é adolescente")
else:
  print("Você não existe ainda.")
