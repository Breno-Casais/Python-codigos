
"""
idade = [1,2,3,4]
idade.remove(2)
print(idade)


teste = [1,2,[3,4]]
teste.remove([3,4])
print(teste)


exercicio
"""
n = int(input("write the number of element of list:"))
lista = []
for i in range(n):
    numero = int(input("write the %i number of list"%i))
    lista.append(numero)
novalista=[]
for i in range(n):
    numero = lista[i]
    if novalista.count(numero) == 0:
        novalista.append(numero)
print(novalista)
