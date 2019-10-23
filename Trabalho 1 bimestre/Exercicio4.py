from time import sleep
def valorPagamento():
    prestacao = int(input("Valor da prestação: "))
    totalJuros = 0
    totalPrestacao = 0
    totalDia = 0
    while prestacao != 0:
        diasAtraso = int(input("Quantos dias atrasado: "))
        if prestacao > 0:
            if diasAtraso > 0:
                valorPagar = (prestacao * 0.03) + (prestacao * (diasAtraso * 0.001)) + prestacao
                totalJuros = valorPagar + totalJuros
            elif diasAtraso == 0:
                totalPrestacao = totalPrestacao + prestacao
            totalDia = totalPrestacao + totalJuros
        elif prestacao == 0:
            print("Finalizando programa...")
            sleep(2)
            break
        elif prestacao < 0:
            print("Opção invalida")
        prestacao = int(input("Valor da prestação: "))
    print("O valor recebido no dia foi de R$" ,totalDia)
    print("Obrigado.")

pagar = valorPagamento()