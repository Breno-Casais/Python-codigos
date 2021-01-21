def imposto(taxaImposto,custo):
    return custo*(1+(taxaImposto/100))

a = int(input("qual é a porcentagem de imposto"))
b = float(input("qual é o preco do produto"))

print(imposto(a,b))


