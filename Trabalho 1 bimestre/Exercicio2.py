def exercicio02(vet):
    maior = 0
    segundoMaior = 0;
    for i in range(0,5):
        if vet[i] > maior:
            maior = vet[i]
        if segundoMaior < maior:
            segundoMaior = vet[i] - 1
    print(maior)
    print(segundoMaior)
vetor = []
for i in range(0, 5):
    vetor.append(int(input('Informe um numero: ')))
m = exercicio02(vetor)
