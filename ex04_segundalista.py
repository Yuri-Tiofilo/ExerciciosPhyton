tipodeVinho = input('tipo de vinho: ')
quantidade = 0
porcentagem = 0
porcentagem2 = 0
porcentagem3 = 0
while tipodeVinho != 'F':
    quantidade = quantidade + 1
    tipodeVinho = input('tipo de vinho: ')
    if tipodeVinho == 'T':
        porcentagem = porcentagem + 1
    elif tipodeVinho == 'B':
        porcentagem2 = porcentagem2 + 1
    else:
        porcentagem3 = porcentagem3 + 1

    amostargem1 = (porcentagem /100) * quantidade
    amostargem2 = (porcentagem2 / 100) * quantidade
    amostargem3 = (porcentagem3 / 100)* quantidade
print(amostargem1,amostargem2,amostargem3)
