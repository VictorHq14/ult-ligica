capital = float(input("digite sua capital:  "))
taxadejuros = float(input("juros aqui sem o %:  "))
tempo = float(input("tempo aqui:  "))
taxadejuro =  taxadejuros / 100

valor = capital * tempo * taxadejuro

print(valor)