""" Peso das provas"""


def Soma(*num):
    soma = 0
    for i in num:
        soma += i
    return soma


def Media(p1, p2, p3, peso1=1, peso2=1, peso3=1):
    return (p1 * peso1 + p2 * peso2 + p3 * peso3) / Soma(peso1 + peso2 + peso3)


print(Media(3,4,3,4,8,7))
