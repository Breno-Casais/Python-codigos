""" o asterisco significa que eu nao sei quenaos elementos eu vou colocar  """


def Soma(num2,*lista):
    num = 0
    for i in lista:
        num += i
    return num


a = [1, 2, 3, 4]

print(Soma(1,2,3,4,5))
