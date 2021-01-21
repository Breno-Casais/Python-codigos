def soma(a ,b,c):
    return a+b+c , b+c


a = int(input("digite o primeiro numero"))
b = int(input("digite o segundo numero"))
c = int(input("digite o terceiro numero"))

print(soma(a,b,c))
a = soma(a,b,c)
b = [6,9]
print(a[0])

if(a[0] > b[0]):
    print("sim")