Caixa = 0
contas = [{123456,0}]
valor = 1

def menu():
    print(" 1- criar uma conta")
    print(" 2-Fechar o programa")


def CriarConta(conta, valor=0):
    valor = int(input("digite o valor a ser colocado na conta"))
    BankAccont = [conta, valor]
    contas.append(BankAccont)


def MostrarSaldo(conta):
    return contas[conta][1]


def ProcurarConta(conta):
    global i
    procurando = -1
    for i in contas:
        if contas[i][0] == conta:
            procurando = i
    return i

while (valor == 1) or (valor == 2):
    conta = int(input(menu()))
    if conta == 2:
        print("muito obrigado por acessar o programa, ate mais")
        valor = -1
    else:
        senha = int(input("digite o numero da conta com 6 digitos"))
        verdadeiro = ProcurarConta(senha)
        if verdadeiro != -1:
            print("o valor da conta é " + MostrarSaldo(verdadeiro))
        else:
            CriarConta(senha)

for i in contas:
    print(contas[i])
