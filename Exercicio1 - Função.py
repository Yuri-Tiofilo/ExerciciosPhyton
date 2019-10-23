def calc_media(vet):
    m = 0
    for i in range (0,5):
        m += vet[i]
    m = m/5
    return m
vet = []
for i in range (0,5):
    vet.append(int(input('Digite o numero: ')))

media = calc_media(vet)
print('A media é igual a %2f' %media)