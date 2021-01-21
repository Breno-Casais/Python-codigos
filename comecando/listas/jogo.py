import random
Ninimigos = int(input("digite o numero de inimigos"))
vida = 500
sp = 100

Ivida = []

for i in range(0, Ninimigos):

    Ivida.append([i,20])

while (vida !=0 or Ninimigos != 0):
    print(vida,sp)
    opcao = int(input('Deseja atacar (1) ou curar (2)'))
    if opcao == 1:

        dano = random.randint(10, 15)
        quemsofreu = random.randint(0,Ninimigos-1)
        Ivida[quemsofreu][1] = ((Ivida[quemsofreu][1]) - dano)
        print('causou %i de dano no inimico %i' % (dano, quemsofreu))

        if Ivida[quemsofreu][1] <= 0:
            Ivida.remove([quemsofreu,Ivida[quemsofreu][1]])
            Ninimigos = Ninimigos-1
            print(Ivida,Ninimigos)


        for i in range(Ninimigos):
            dano = random.randint(0,3)
            vida = vida - dano
            print('o inimigo %i causou %i de dano' % (i, dano))

    else:
        if sp> 10:
            cura = random.randint(0,15)
            for i in range(Ninimigos):
                dano = random.randint(0, 3)
                vida = vida - dano
                print('o inimigo %i causou %i de dano' % (i, dano))
            sp = sp-10
        else:
            print('voce nao tem sp para se curar')
            sp = sp -3
    sp = sp+3
    if sp > 100:
        sp = 100
    if Ninimigos == 0:
        vida = 0

