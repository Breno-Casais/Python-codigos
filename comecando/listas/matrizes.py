def controiMatriz(m,n,matriz):
    for i in range(1,m+1):
        linha = []
        for j in range(1,n+1):
            x = int(input("digite o valor %i%i da matriz :"%(i,j)))
            linha.append(x)
        matriz.append(linha)

def trocaelemento(pos1,pos2,matriz):
    elemento1 = matr 

matriz = []
m = int(input("digite o numero de linhas da matriz"))
n = int(input("digite o numero de colunas da matriz"))

controiMatriz(m,n,matriz)
print(matriz)

