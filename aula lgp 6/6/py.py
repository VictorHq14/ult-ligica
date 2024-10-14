preço = float(input("digite o valor de um produto sem desconto: "))
desc = float(input("digite o desconto em % mas sem o sinal de % : "))
menorizadore = desc / 100
desconto = preço * menorizadore
descontovalor = preço - desconto

print(descontovalor)