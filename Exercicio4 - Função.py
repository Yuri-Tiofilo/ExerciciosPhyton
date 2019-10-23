def posicaoImpar(vet):
    soma = 0
    media = 0
    indice = 0
    for i in range (0,5):
        if i % 2 != 0:
            soma += vet[i]
            indice = indice + 1
    media = soma / indice
    return media

vetor = []
for i in range(0,5):
    vetor.append(int(input('Informe um numero: ')))
m = posicaoImpar(vetor)
print(m)