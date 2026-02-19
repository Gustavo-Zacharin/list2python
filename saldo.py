s = 500

while True:
    r = float(input(" MENU: (1) Depositar  (2)Sacar  (3)Sair: "))

    if r == 1:
        d = float(input("Deposite uma quantia: "))
        s += d
        print(f"Foi depositado R${d}, portanto seu saldo de agora é de: R${s} ")
    elif r == 2:
        sacar = float(input(f"Saque uma quantia, lembrando que seu saldo é de R${s}: "))
        s -= sacar
        if sacar > s:
            print("Saldo insuficiente!")
        elif sacar <= 0:
            print("Desculpe saque uma quantia verdadeira!")
        else:
            print(f"Foi sacado {sacar}, portanto seu saldo restante é de: R${s}")
    elif r == 3:
        print("Você saiu!")
        break
    else:
        print("Digite um número dentre esses 3!")