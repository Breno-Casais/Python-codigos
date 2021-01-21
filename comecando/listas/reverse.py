idade = []
altura = []

for i in range(5):

    idades = int(input('digite sua idade:'))
    alturas = float(input('digite sua altura:'))

    idade.append(idades)
    altura.append(alturas)

idade.reverse()
altura.reverse()

for i in range(5):

    print(idade[i],altura[i])