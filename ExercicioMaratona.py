entrada = int(input())
pares = []
impares = []
for i in range (0,entrada):
    num = int(input())
    if (num > 0):
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)

    pares.sort()
    impares.sort(reverse = True)

    for p in pares:
        print(p)

    for i in impares:
        print(i)

