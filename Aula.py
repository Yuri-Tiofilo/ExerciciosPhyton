lado1 = int(input('Digite o segmento 1: '))
lado2 = int(input('Digite o segmento 2: '))
lado3 = int(input('Digite o segmento 3: '))
if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado3:
    if lado1 == lado2 == lado3:
        print('EQUILATERO')
    elif lado1 == lado2 or lado2 == lado3 or lado3 == lado1:
        print('ISOCELES')
    else:
        print('Esclaeno')
else:
    print('Não é triangulo')