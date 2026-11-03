#Materia de recuperação

for i in range(10, 1, -1):
    print("Executando o comando número:", i+1)
    print("Olá")

    #

    i = 1  
    while i < 10:
        print("Executando o comando número:", i+1)
        print("Olá")
        i = i + 1

    #

    valor = 0  
    while valor != 5:
        print("Executando o comando número:", valor+1)
        print("Olá")
        valor = valor + 1

print("Obrigado você digitou 5")

#

Saldo = int(input("Digite o saldo disponivel: "))
comprando = True
while Saldo >= 5 and comprando:
    print("Você pode fazer uma compra!")
    Saldo -= 5
    resposta = int(
        input("Digite 1 para continuar comprando ou 0 para sair: "))
            comprando = False
            print("Você saiu do loop de compras.")



    # Aqui você pode adicionar o código para realizar a compra

