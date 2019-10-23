vet = []
soma = 0
par = 0
media = 0
media2 = 0
for i in range(0,5):
    vet.append(float(input('Informe a nota: ')))

for i in range(0,5):
    soma = soma + vet[i]
    if vet[i] % 2 == 0:
        par = par + 1
        media = media = vet[i]

for i in range(0,5):
    media2 = soma / 5
    if soma > media2:
        print('Aprovado')
    else:
        print('Reprovado')
print('Media dos pares: ', media/par)
print('A soma das notas é: ',soma)
