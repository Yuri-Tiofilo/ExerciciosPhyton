def maiorVetor(vet):
    maior = 0
    for i in range (0,5):
        if vet[i] > maior:
            maior = vet[i]
    return maior
vetor = []
for i in range(0, 5):
    vetor.append(int(input('Informe um numero: ')))
maior = maiorVetor(vetor)
print(maior)


