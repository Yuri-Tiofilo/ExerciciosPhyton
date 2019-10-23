def exercicioSete(numero):
    fatorial = 1
    while numero > 0:
        fatorial *= numero
        numero -= 1

    return fatorial
num = int(input('Digite um numero: '));
fat = exercicioSete(num)
print(fat)