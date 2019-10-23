from time import sleep
def tabuada():
    n = int(input('Digite um valor que voce quer saber a tabuada de 1 ao 10: '))
    n1 = n * 1
    n2 = n * 2
    n3 = n * 3
    n4 = n * 4
    n5 = n * 5
    n6 = n * 6
    n7 = n * 7
    n8 = n * 8
    n9 = n * 9
    n10 = n * 10
    print('Resultado de {}x1: {}'.format(n, n1))
    print('Resultado de {}x2: {}'.format(n, n2))
    print('Resultado de {}x3: {}'.format(n, n3))
    print('Resultado de {}x4: {}'.format(n, n4))
    print('Resultado de {}x5: {}'.format(n, n5))
    print('Resultado de {}x6: {}'.format(n, n6))
    print('Resultado de {}x7: {}'.format(n, n7))
    print('Resultado de {}x8: {}'.format(n, n8))
    print('Resultado de {}x9: {}'.format(n, n9))
    print('Resultado de {}x10: {}'.format(n, n10))

def IMC():
    print('=====CALCULANDO SEU IMC!=====')
    print(' ')
    peso = float(input('Qual o seu peso atual (KG)? '))
    altura = float(input('Qual a sua altura (M)? '))
    imc = (peso / (altura * altura))
    print('Calculando seu IMC...')
    sleep(2)
    print('Seu IMC é {:.2f}, e voce esta '.format(imc), end='')
    if imc < 18.5:
        print('ABAIXO DO PESO!')
        print('COMA MAIS!')
    elif imc >= 18.5 and imc < 25:
        print('COM O PESO IDEAL!')
        print('PARABÉNS, CONTINUE ASSIM!')
    elif imc >= 25 and imc < 30:
        print('COM SOBREPESO!')
        print('CUIDADO COM SEU PESO!')
    elif imc >= 30 and imc < 40:
        print('COM OBESIDADE!')
        print('COMECE UM REGIME URGENTE E FECHE A BOCA!')
    else:
        print('COM OBESIDADE MÓRBIDA!')
        print('PROCURE UM PROFISSIONAL URGENTE!')

def fatorial():
    n = int(input('Digite um numero para calcular seu fatorial: '))
    c = n
    f = 1
    print('Calculando {}! = '.format(n), end='')
    while c > 0:
        print('{}'.format(c), end='')
        print(' x ' if c > 1 else ' = ', end='')
        f *= c
        c -= 1
    print('{}'.format(f))

opcao = 0
while opcao != -1:
    print('''    
        [1] Tabuada
        [2] IMC
        [3] Fatorial
        [-1] Sair do programa''')
    opcao = int(input("Qual a sua opção: "))
    if opcao == 1:
        tabuada()
    elif opcao == 2:
        IMC()
    elif opcao == 3:
        fatorial()
    elif opcao == -1:
        break
    else:
        print("Opção invalida")
print("Finalizando programa...")
sleep(2)
print("Obrigado.")