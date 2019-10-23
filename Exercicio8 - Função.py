def somatoria():
    N = int(input("Digite um Numero:"))
    I = 1
    S = 0
    while I <= N:
        S = S + (I/(I*I))
        I = I + 1
    print("Somatória: ", S)

S = somatoria()