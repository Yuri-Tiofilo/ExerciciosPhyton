def exercicio03(n):
  for i in range(1, n+1):
    for j in range(i):
      print (j+1, end=" ")
    print('')
numero = int(input('numero: '))
m = exercicio03(numero)
