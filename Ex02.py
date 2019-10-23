

capital = int(input('Digite o valor do capital: '))
mes = int(input('Digite o numero de mês: '))
j = 0
mesinit = 0
while mesinit < mes:
    mesinit += 1
    j = (capital/100)*10
    capital = j + capital
    print('{:.2f}'.format(capital))

for mesinit in range(mes):
    mesinit += 1
    j = (capital / 100) * 10
    capital = j + capital
    print('{:.2f}'.format(capital))
    
