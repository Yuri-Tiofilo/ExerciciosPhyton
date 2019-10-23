def verifica(l1,l2,l3):
    caso1 = l2 + l3
    caso2 = (l2 ** 2) + (l3 ** 2);
    if l1 > caso1:
        print('Isto não é um triângulo!');
    elif ((l1 ** 2) == caso2):
        print('Triângulo retângulo')
    elif  ((l1 ** 2) > caso2):
        print('Triângulo obtuso');
    else:
        print('Triângulo acutângulo');

lado1 = int(input('Digite o valor do primeiro lado:'))
lado2 = int(input('Digite o valor do segundo lado:'))
lado3 = int(input('Digite o valor do terceiro lado:'))
n = verifica(lado1, lado2, lado3)
print(n)