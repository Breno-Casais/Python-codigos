X: int = 0
def incremeta(x):
    global X
    x += 1
    print(x)

y = 10
incremeta(y)
print(y)