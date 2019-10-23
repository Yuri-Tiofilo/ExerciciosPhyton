
tipocombustivel = input('Digite o tipo de combustivel G- Gasolina, A- Alcool:  ')
qtdelitros = float(input('Digite a quantidade de litros de combustivel: '))
if tipocombustivel == 'A':
    if qtdelitros <= 20:
        desconto = 0.3 * qtdelitros * 2.10
        valor = qtdelitros * 2.10 - desconto
    elif qtdelitros > 20:
        desconto = 0.5 * qtdelitros * 2.10
        valor = qtdelitros * 2.10 - desconto
elif tipocombustivel == 'G':
    if qtdelitros <= 20:
        desconto = 0.4 * qtdelitros * 3.30
        valor = qtdelitros * 3.30 - desconto
    elif qtdelitros > 20:
        desconto = 0.5 * qtdelitros * 3.30
        valor = qtdelitros * 3.30 - desconto

print('O valor total a pagar é de: %.2f' % valor)